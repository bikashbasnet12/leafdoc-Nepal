import os
import re
import base64
import numpy as np
import onnxruntime as ort
from PIL import Image
from flask import Flask, render_template, request, jsonify
from disease_info import get_info

app = Flask(__name__)

# ====== CONFIG ======
MODEL_PATH = "model.onnx"
CLASSES_PATH = "classes.txt"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ====== LOAD CLASSES ======
with open(CLASSES_PATH) as f:
    class_names = [line.strip() for line in f.readlines()]

num_classes = len(class_names)

# ====== LOAD ONNX MODEL ======
session = ort.InferenceSession(MODEL_PATH)
input_name = session.get_inputs()[0].name
print(f"ONNX model loaded. Classes: {class_names}")

# ====== TRANSFORMS ======
MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

def preprocess(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224), Image.LANCZOS)
    arr = np.array(img, dtype=np.float32) / 255.0
    arr = (arr - MEAN) / STD
    arr = arr.transpose(2, 0, 1)
    arr = np.expand_dims(arr, axis=0)
    return arr.astype(np.float32)

# ====== PREDICT FUNCTION ======
def predict_image(image_path):
    tensor = preprocess(image_path)
    outputs = session.run(None, {input_name: tensor})[0]

    exp = np.exp(outputs - outputs.max())
    probabilities = exp / exp.sum()

    predicted = int(np.argmax(probabilities))
    confidence = round(float(probabilities[0][predicted]) * 100, 1)

    class_name = class_names[predicted]

    if confidence < 50:
        class_name = "UNKNOWN"

    info = get_info(class_name)
    info["class_name"] = class_name
    info["confidence"] = confidence
    return info

# ====== ROUTES ======
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    source = request.form.get("source", "upload")

    # ── Step 1: Get the image (camera OR upload) ──
    if source == "camera":
        camera_data = request.form.get("camera_data", "")
        if not camera_data:
            return jsonify({"error": "No camera image captured"}), 400

        image_data = re.sub(r'^data:image/.+;base64,', '', camera_data)
        image_bytes = base64.b64decode(image_data)

        filename = "camera_capture.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(image_bytes)

    else:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

    # ── Step 2: Run AI inference (runs for BOTH camera and upload) ──
    result = predict_image(filepath)
    result_class = result["class_name"]
    result_confidence = result["confidence"]

    # ── Step 3: Language ──
    lang = request.form.get("lang", "en")
    if lang not in ["en", "ne"]:
        lang = "en"

    # ── Step 4: Get full bilingual info ──
    info = get_info(result_class)

    # ── Step 5: Build response object ──
    localized_data = {
        "plant_en":      info["plant"]["en"],
        "plant_ne":      info["plant"]["ne"],
        "disease_en":    info["disease"]["en"],
        "disease_ne":    info["disease"]["ne"],
        "severity_en":   info["severity"]["en"],
        "severity_ne":   info["severity"]["ne"],
        "treatment_en":  info["treatment"]["en"],
        "treatment_ne":  info["treatment"]["ne"],
        "fertilizer_en": info["fertilizer"]["en"],
        "fertilizer_ne": info["fertilizer"]["ne"],
        "color":         info["color"],
        "buy_links":     info["buy_links"],
        "image_path":    "/" + filepath,
        "confidence":    result_confidence,
    }

    # ── Step 6: Return JSON for mobile, HTML for web ──
    if request.form.get("client") == "mobile" or request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"status": "success", "data": localized_data})
    else:
        return render_template("result.html", result=localized_data)

if __name__ == "__main__":
    app.run(debug=True)
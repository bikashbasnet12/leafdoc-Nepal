import os
import gc
import base64
import re
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
from flask import Flask, render_template, request, jsonify
from disease_info import get_info

app = Flask(__name__)

# ====== CONFIG ======
MODEL_PATH = "model.pth"
CLASSES_PATH = "classes.txt"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ====== LOAD CLASSES ======
with open(CLASSES_PATH) as f:
    class_names = [line.strip() for line in f.readlines()]

num_classes = len(class_names)

# ====== LOAD MODEL (CPU only, memory optimized) ======
device = torch.device("cpu")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# Free unused memory after loading
gc.collect()
torch.set_num_threads(1)  # limit CPU threads to reduce memory

print(f"Model loaded. Classes: {class_names}")

# ====== TRANSFORMS ======
transform = transforms.Compose([
    transforms.Resize((128, 128)),   # reduced from 224 to save memory
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# ====== PREDICT FUNCTION ======
def predict_image(image_path):
    img = Image.open(image_path).convert("RGB")

    # Resize image before processing to save memory
    img = img.resize((256, 256), Image.LANCZOS)

    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    # Free memory immediately after prediction
    del tensor, outputs, probabilities
    gc.collect()

    class_name = class_names[predicted.item()]
    conf_percent = round(confidence.item() * 100, 1)

    if conf_percent < 50:
        class_name = "UNKNOWN"

    info = get_info(class_name)
    info["class_name"] = class_name
    info["confidence"] = conf_percent
    return info

# ====== ROUTES ======
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    source = request.form.get("source", "upload")

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

    result = predict_image(filepath)
    result["image_path"] = "/" + filepath

    # Clean up uploaded file after prediction to save disk space
    try:
        if os.path.exists(filepath):
            pass  # keep for display, will be overwritten next upload
    except:
        pass

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
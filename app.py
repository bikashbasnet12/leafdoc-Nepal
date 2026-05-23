import os
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

# ====== LOAD MODEL ======
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()
model.to(device)

print(f"Model loaded. Classes: {class_names}")

# ====== TRANSFORMS ======
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# ====== PREDICT FUNCTION ======
def predict_image(image_path):
    img = Image.open(image_path).convert("RGB")
    tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    class_name = class_names[predicted.item()]
    conf_percent = round(confidence.item() * 100, 1)

    # Low confidence → treat as unknown
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
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = predict_image(filepath)
    result["image_path"] = "/" + filepath

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
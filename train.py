import os
import ssl
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split, Subset
import random

ssl._create_default_https_context = ssl._create_unverified_context

# ====== SETTINGS ======
DATA_DIR = "dataset"
BATCH_SIZE = 16        # smaller = less RAM usage
EPOCHS = 10
LR = 0.001
MODEL_PATH = "model.pth"
CLASSES_PATH = "classes.txt"
MAX_PER_CLASS = 1000  

# ====== DEVICE (uses Apple M4 chip if available) ======
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print(f"Using device: {device}")

# ====== TRANSFORMS ======
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225]),
])

# ====== LOAD FULL DATASET ======
full_dataset = datasets.ImageFolder(DATA_DIR, transform=transform)
num_classes = len(full_dataset.classes)

# Save class names
with open(CLASSES_PATH, "w") as f:
    for cls in full_dataset.classes:
        f.write(cls + "\n")

print(f"Found {num_classes} classes: {full_dataset.classes}")
print(f"Total images in dataset: {len(full_dataset)}")

# ====== LIMIT IMAGES PER CLASS (important!) ======
# Group indices by class
class_indices = {i: [] for i in range(num_classes)}
for idx, (_, label) in enumerate(full_dataset.samples):
    class_indices[label].append(idx)

# Pick max MAX_PER_CLASS images per class randomly
selected_indices = []
for label, indices in class_indices.items():
    if len(indices) > MAX_PER_CLASS:
        selected = random.sample(indices, MAX_PER_CLASS)
    else:
        selected = indices
    selected_indices.extend(selected)
    print(f"  {full_dataset.classes[label]}: using {len(selected)} images")

random.shuffle(selected_indices)
limited_dataset = Subset(full_dataset, selected_indices)
print(f"\nUsing {len(limited_dataset)} images total (max {MAX_PER_CLASS} per class)")

# ====== TRAIN / VAL SPLIT (80/20) ======
val_size = int(0.2 * len(limited_dataset))
train_size = len(limited_dataset) - val_size
train_dataset, val_dataset = random_split(limited_dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
val_loader   = DataLoader(val_dataset,   batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

print(f"Train: {train_size} | Val: {val_size}\n")
print("Downloading  model...")
model = models.resnet18(weights="IMAGENET1K_V1")

# Freeze base layers
for param in model.parameters():
    param.requires_grad = False

# Replace final layer for our classes
model.fc = nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)
print("Model ready.\n")

# ====== LOSS & OPTIMIZER ======
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=LR)

# ====== TRAINING ======
best_val_acc = 0.0

for epoch in range(EPOCHS):
    # --- Train ---
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for batch_idx, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        # Print progress every 10 batches
        if (batch_idx + 1) % 10 == 0:
            print(f"  Epoch {epoch+1} | Batch {batch_idx+1}/{len(train_loader)} | Loss: {loss.item():.4f}")

    train_acc = 100 * correct / total

    # --- Validate ---
    model.eval()
    val_correct = 0
    val_total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            val_total += labels.size(0)
            val_correct += (predicted == labels).sum().item()

    val_acc = 100 * val_correct / val_total

    print(f"\nEpoch [{epoch+1}/{EPOCHS}] | Loss: {running_loss:.4f} | Train: {train_acc:.1f}% | Val: {val_acc:.1f}%")

    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), MODEL_PATH)
        print(f"  ✅ Best model saved (Val Acc: {val_acc:.1f}%)\n")
    else:
        print()

print(f"Training complete! Best Val Accuracy: {best_val_acc:.1f}%")
print(f"Model saved: {MODEL_PATH}")
print(f"Classes saved: {CLASSES_PATH}")
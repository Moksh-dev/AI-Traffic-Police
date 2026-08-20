from ultralytics import YOLO
from pathlib import Path

# Load the pretrained YOLO model
model = YOLO("yolo26n.pt")

# Path to our dataset training folder
dataset_path = Path("Vehicles-coco.v2i.multiclass/train")

# Find all JPG images in the folder
images = list(dataset_path.glob("*.jpg"))

# Select the first image
image_path = images[0]

print(f"Testing image: {image_path}")

# Run YOLO detection
results = model.predict(
    source=str(image_path),
    save=True
)

print("Detection completed successfully!")
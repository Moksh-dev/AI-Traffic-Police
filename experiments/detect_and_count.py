from ultralytics import YOLO
from pathlib import Path

# Load the pretrained YOLO model
model = YOLO("yolo26n.pt")

# Path to our dataset
dataset_path = Path("Vehicles-coco.v2i.multiclass/train")

# Get all JPG images
images = list(dataset_path.glob("*.jpg"))

# Select an image
image_path = images[0]

print(f"\nProcessing image: {image_path}")

# Run YOLO with a confidence threshold
results = model.predict(
    source=str(image_path),
    conf=0.25,
    save=True
)

# Get the result for this image
result = results[0]

# Vehicle classes we want
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

# Initialize counts
vehicle_counts = {
    "car": 0,
    "motorcycle": 0,
    "bus": 0,
    "truck": 0
}

print("\nDETECTED VEHICLES")
print("-" * 30)

# Go through every detected object
for box in result.boxes:

    # Get class ID
    class_id = int(box.cls[0])

    # Convert class ID to class name
    class_name = result.names[class_id]

    # Get confidence score
    confidence = float(box.conf[0])

    # Keep only vehicle classes
    if class_name in vehicle_classes:

        vehicle_counts[class_name] += 1

        print(
            f"{class_name} | "
            f"confidence: {confidence:.2f}"
        )

# Print final counts
print("\nFINAL VEHICLE COUNT")
print("-" * 30)

for vehicle, count in vehicle_counts.items():
    print(f"{vehicle}: {count}")
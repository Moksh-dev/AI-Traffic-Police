from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo26n.pt")

# Run detection
results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True
)

# Get the first result
result = results[0]

# Vehicle classes we want to count
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

# Create a dictionary to store counts
vehicle_counts = {
    "car": 0,
    "motorcycle": 0,
    "bus": 0,
    "truck": 0
}

# Loop through every detected object
for class_id in result.boxes.cls:

    # Convert tensor value into a normal Python integer
    class_id = int(class_id)

    # Get the class name
    class_name = result.names[class_id]

    # Count only vehicles
    if class_name in vehicle_classes:
        vehicle_counts[class_name] += 1

# Print the final counts
print("\nVEHICLE COUNT RESULTS")
print("-" * 30)

for vehicle, count in vehicle_counts.items():
    print(f"{vehicle}: {count}")
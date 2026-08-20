from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Run object detection on a sample traffic image
results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True
)

print("Detection completed successfully!")
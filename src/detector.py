from ultralytics import YOLO


class VehicleDetector:

    # COCO class IDs for vehicles
    VEHICLE_CLASSES = {
        2: "car",
        3: "motorcycle",
        5: "bus",
        7: "truck"
    }

    def __init__(self, model_path="../yolo26n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image, confidence=0.5):
        results = self.model.predict(
            source=image,
            conf=confidence,
            classes=list(self.VEHICLE_CLASSES.keys())
        )

        return results[0]
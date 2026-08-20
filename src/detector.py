import os

from ultralytics import YOLO


class VehicleDetector:
    def __init__(self):
        # Get the absolute path of the project root
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        # Build the model path
        model_path = os.path.join(
            project_root,
            "models",
            "yolo26n.pt"
        )

        # Load the locally stored YOLO model
        self.model = YOLO(model_path)

        # COCO class IDs for supported vehicles
        self.vehicle_classes = {
            2: "car",
            3: "motorcycle",
            5: "bus",
            7: "truck"
        }

    def detect(self, source, confidence=0.4):
        results = self.model.predict(
            source=source,
            conf=confidence,
            verbose=False
        )

        return results[0]
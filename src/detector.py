from pathlib import Path
from ultralytics import YOLO


class VehicleDetector:

    def __init__(self):
        # Find the project root directory
        project_root = Path(__file__).resolve().parent.parent

        # Full path to the YOLO model
        model_path = project_root / "yolo26n.pt"

        # Load pretrained YOLO
        self.model = YOLO(str(model_path))

    def detect(self, image_path, confidence=0.25):

        results = self.model.predict(
            source=image_path,
            conf=confidence,
            save=False
        )

        return results[0]
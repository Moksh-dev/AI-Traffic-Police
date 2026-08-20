class VehicleCounter:

    def __init__(self):

        self.vehicle_classes = [
            "car",
            "motorcycle",
            "bus",
            "truck"
        ]

    def process_vehicles(self, result):

        vehicle_counts = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

        detected_vehicles = []

        # Go through every bounding box detected by YOLO
        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = result.names[class_id]

            confidence = float(box.conf[0])

            # Bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            if class_name in self.vehicle_classes:

                vehicle_counts[class_name] += 1

                vehicle = {
                    "class": class_name,
                    "confidence": round(confidence, 2),
                    "bbox": {
                        "x1": round(x1, 2),
                        "y1": round(y1, 2),
                        "x2": round(x2, 2),
                        "y2": round(y2, 2)
                    }
                }

                detected_vehicles.append(vehicle)

        return vehicle_counts, detected_vehicles
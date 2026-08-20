class VehicleCounter:

    def count(self, result):
        vehicle_counts = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

        if result.boxes is None:
            return vehicle_counts

        for box in result.boxes:
            class_id = int(box.cls[0])

            if class_id == 2:
                vehicle_counts["car"] += 1

            elif class_id == 3:
                vehicle_counts["motorcycle"] += 1

            elif class_id == 5:
                vehicle_counts["bus"] += 1

            elif class_id == 7:
                vehicle_counts["truck"] += 1

        return vehicle_counts
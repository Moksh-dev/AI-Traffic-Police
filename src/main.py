from pathlib import Path
import cv2

from detector import VehicleDetector
from vehicle_counter import VehicleCounter


def main():

    # Find the project root directory
    project_root = Path(__file__).resolve().parent.parent

    # Create the detector
    detector = VehicleDetector()

    # Create the vehicle processor
    counter = VehicleCounter()

    # Path to input traffic image
    image_path = (
        project_root
        / "data"
        / "images"
        / "traffic.jpg"
    )

    # Check if image exists
    if not image_path.exists():
        print("Error: Input image not found!")
        print(f"Expected image at: {image_path}")
        return

    print("\nProcessing image...")
    print(f"Image: {image_path}")

    # STEP 1: Detect objects using YOLO
    result = detector.detect(str(image_path))

    # STEP 2: Process detected vehicles
    vehicle_counts, detected_vehicles = counter.process_vehicles(result)

    # STEP 3: Display vehicle counts
    print("\nVEHICLE COUNT RESULTS")
    print("-" * 30)

    for vehicle, count in vehicle_counts.items():
        print(f"{vehicle}: {count}")

    # STEP 4: Display detailed vehicle information
    print("\nDETECTED VEHICLE DETAILS")
    print("-" * 30)

    for index, vehicle in enumerate(detected_vehicles, start=1):
        print(f"\nVehicle {index}")
        print(f"Type: {vehicle['class']}")
        print(f"Confidence: {vehicle['confidence']}")
        print(f"Bounding Box: {vehicle['bbox']}")

    # STEP 5: Generate annotated image
    annotated_image = result.plot()

    # Output image path
    output_path = (
        project_root
        / "outputs"
        / "images"
        / "traffic_result.jpg"
    )

    # Make sure output folder exists
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save annotated image
    cv2.imwrite(
        str(output_path),
        annotated_image
    )

    print("\nAnnotated image saved successfully!")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
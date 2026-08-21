import argparse
import csv
import os
from pathlib import Path

from detector import VehicleDetector
from vehicle_counter import VehicleCounter


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}


def find_images(dataset_path):
    """Find all supported image files inside the dataset directory."""

    image_paths = []

    for file_path in Path(dataset_path).rglob("*"):
        if file_path.suffix.lower() in IMAGE_EXTENSIONS:
            image_paths.append(file_path)

    return image_paths


def evaluate_dataset(dataset_path):
    """Run vehicle detection evaluation on all images in a dataset."""

    print("\n" + "=" * 60)
    print("              DATASET EVALUATION")
    print("=" * 60)

    print(f"\nDataset: {dataset_path}")
    print("\nSearching for images...")

    image_paths = find_images(dataset_path)

    if not image_paths:
        print("\nNo supported images found in the specified dataset.")
        return

    print(f"Images found: {len(image_paths)}")

    detector = VehicleDetector()
    counter = VehicleCounter()

    total_images = 0
    images_with_vehicles = 0

    total_counts = {
        "car": 0,
        "motorcycle": 0,
        "bus": 0,
        "truck": 0
    }

    print("\nStarting evaluation...\n")

    for index, image_path in enumerate(image_paths, start=1):

        try:
            result = detector.detect(str(image_path))

            counts = counter.count(result)

            total_detected = sum(counts.values())

            total_images += 1

            if total_detected > 0:
                images_with_vehicles += 1

            for vehicle_type in total_counts:
                total_counts[vehicle_type] += counts[vehicle_type]

            if index % 50 == 0 or index == len(image_paths):
                print(
                    f"Processed {index}/{len(image_paths)} images"
                )

        except Exception as error:
            print(
                f"\nError processing {image_path.name}: {error}"
            )

    total_vehicles = sum(total_counts.values())

    if total_images > 0:
        average_vehicles = total_vehicles / total_images

        detection_rate = (
            images_with_vehicles / total_images
        ) * 100
    else:
        average_vehicles = 0
        detection_rate = 0

    print("\n" + "=" * 60)
    print("           DATASET EVALUATION REPORT")
    print("=" * 60)

    print(f"\nDataset: {dataset_path}")
    print(f"Images processed: {total_images}")
    print(f"Images with vehicles detected: {images_with_vehicles}")
    print(f"Vehicle detection rate: {detection_rate:.2f}%")

    print("\nTOTAL VEHICLE DETECTIONS")
    print("-" * 60)

    print(f"Cars:        {total_counts['car']}")
    print(f"Motorcycles: {total_counts['motorcycle']}")
    print(f"Buses:       {total_counts['bus']}")
    print(f"Trucks:      {total_counts['truck']}")

    print("-" * 60)
    print(f"Total vehicles detected: {total_vehicles}")
    print(f"Average vehicles per image: {average_vehicles:.2f}")

    print("=" * 60)

    save_report(
        dataset_path,
        total_images,
        images_with_vehicles,
        detection_rate,
        total_counts,
        total_vehicles,
        average_vehicles
    )


def save_report(
    dataset_path,
    total_images,
    images_with_vehicles,
    detection_rate,
    total_counts,
    total_vehicles,
    average_vehicles
):
    """Save evaluation results as a CSV file."""

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    output_directory = os.path.join(
        project_root,
        "outputs",
        "evaluation"
    )

    os.makedirs(output_directory, exist_ok=True)

    # Get the dataset folder name instead of the final 'train' folder.
    #
    # Example:
    # datasets/Vehicles-coco.v2i.multiclass/train
    #                    ↑
    #        This becomes the report name.
    dataset_path_object = Path(dataset_path)

    dataset_name = dataset_path_object.parent.name

    report_path = os.path.join(
        output_directory,
        f"{dataset_name}_evaluation.csv"
    )

    with open(
        report_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        writer.writerow(
            ["Dataset", dataset_name]
        )

        writer.writerow(
            ["Dataset Path", dataset_path]
        )

        writer.writerow(
            ["Images Processed", total_images]
        )

        writer.writerow(
            ["Images with Vehicles Detected", images_with_vehicles]
        )

        writer.writerow(
            ["Detection Rate (%)", f"{detection_rate:.2f}"]
        )

        writer.writerow(
            ["Cars Detected", total_counts["car"]]
        )

        writer.writerow(
            ["Motorcycles Detected", total_counts["motorcycle"]]
        )

        writer.writerow(
            ["Buses Detected", total_counts["bus"]]
        )

        writer.writerow(
            ["Trucks Detected", total_counts["truck"]]
        )

        writer.writerow(
            ["Total Vehicle Detections", total_vehicles]
        )

        writer.writerow(
            [
                "Average Vehicles Per Image",
                f"{average_vehicles:.2f}"
            ]
        )

    print("\nEvaluation report saved to:")
    print(report_path)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the AI Traffic Police "
            "vehicle detection pipeline on a dataset"
        )
    )

    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to the dataset folder containing images"
    )

    args = parser.parse_args()

    dataset_path = args.dataset

    if not os.path.exists(dataset_path):
        print("\nERROR: Dataset path does not exist.")
        print(f"Path provided: {dataset_path}")
        return

    evaluate_dataset(dataset_path)


if __name__ == "__main__":
    main()
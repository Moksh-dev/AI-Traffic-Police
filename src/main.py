import argparse
import os
import sys

from detector import VehicleDetector
from vehicle_counter import VehicleCounter


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".wmv"
}


def print_header():
    print("\n" + "=" * 60)
    print("               AI TRAFFIC POLICE")
    print("        Vehicle Detection & Classification")
    print("=" * 60)


def print_counts(vehicle_counts):
    total_vehicles = sum(vehicle_counts.values())

    print("\nVEHICLE COUNT RESULTS")
    print("-" * 60)

    print(f"Cars:        {vehicle_counts['car']}")
    print(f"Motorcycles: {vehicle_counts['motorcycle']}")
    print(f"Buses:       {vehicle_counts['bus']}")
    print(f"Trucks:      {vehicle_counts['truck']}")

    print("-" * 60)
    print(f"TOTAL VEHICLES: {total_vehicles}")
    print("=" * 60)


def process_image(source_path):
    print("\nProcessing image...")
    print(f"Image: {source_path}")

    detector = VehicleDetector()
    counter = VehicleCounter()

    result = detector.detect(source_path)

    vehicle_counts = counter.count(result)

    print_counts(vehicle_counts)

    print("\nDetection completed successfully!")


def process_video(source_path):
    print("\nProcessing video...")
    print(f"Video: {source_path}")

    from video_detector import process_video

    process_video(source_path)


def get_source_type(source_path):
    _, extension = os.path.splitext(source_path)

    extension = extension.lower()

    if extension in IMAGE_EXTENSIONS:
        return "image"

    if extension in VIDEO_EXTENSIONS:
        return "video"

    return None


def main():
    parser = argparse.ArgumentParser(
        description="AI Traffic Police - Vehicle Detection and Counting System"
    )

    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Path to an image or video file"
    )

    args = parser.parse_args()

    source_path = args.source

    print_header()

    if not os.path.exists(source_path):
        print("\nERROR: File not found.")
        print(f"Path provided: {source_path}")
        print("\nPlease check the file path and try again.")
        sys.exit(1)

    source_type = get_source_type(source_path)

    if source_type == "image":
        process_image(source_path)

    elif source_type == "video":
        process_video(source_path)

    else:
        print("\nERROR: Unsupported file format.")
        print("\nSupported image formats:")
        print(", ".join(sorted(IMAGE_EXTENSIONS)))

        print("\nSupported video formats:")
        print(", ".join(sorted(VIDEO_EXTENSIONS)))

        sys.exit(1)


if __name__ == "__main__":
    main()
import os
import cv2

from detector import VehicleDetector
from vehicle_counter import VehicleCounter


def process_video(video_path):
    detector = VehicleDetector()
    counter = VehicleCounter()

    # Open input video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    print("Video opened successfully!")

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Find project root
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Create output directory
    output_directory = os.path.join(
        project_root,
        "outputs",
        "videos"
    )

    os.makedirs(output_directory, exist_ok=True)

    # Create output filename
    input_filename = os.path.basename(video_path)
    filename_without_extension, _ = os.path.splitext(input_filename)

    output_path = os.path.join(
        output_directory,
        f"{filename_without_extension}_processed.mp4"
    )

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    output_video = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (frame_width, frame_height)
    )

    print(f"Processing video...")
    print(f"Output will be saved to:\n{output_path}")

    while True:
        success, frame = cap.read()

        if not success:
            break

        # Detect only vehicles
        result = detector.detect(frame)

        # Count vehicles in the current frame
        counts = counter.count(result)

        total_vehicles = sum(counts.values())

        # Draw bounding boxes
        annotated_frame = result.plot()

        # Create display text
        text = (
            f"Total: {total_vehicles} | "
            f"Cars: {counts['car']} | "
            f"Motorcycles: {counts['motorcycle']} | "
            f"Buses: {counts['bus']} | "
            f"Trucks: {counts['truck']}"
        )

        # Draw vehicle information
        cv2.putText(
            annotated_frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Save processed frame
        output_video.write(annotated_frame)

        # Show processed frame
        cv2.imshow(
            "AI Traffic Police - Vehicle Detection",
            annotated_frame
        )

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("\nProcessing stopped by user.")
            break

    # Release resources
    cap.release()
    output_video.release()
    cv2.destroyAllWindows()

    print("\nVideo processing completed successfully!")
    print(f"Processed video saved to:\n{output_path}")
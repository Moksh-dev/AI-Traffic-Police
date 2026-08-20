import cv2

from detector import VehicleDetector
from vehicle_counter import VehicleCounter


def process_video(video_path):
    # Create our detector and counter
    detector = VehicleDetector()
    counter = VehicleCounter()

    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    print("Video opened successfully!")

    while True:
        # Read the next frame
        success, frame = cap.read()

        if not success:
            break

        # Detect vehicles in the current frame
        result = detector.detect(frame)

        # Count vehicles in the current frame
        counts = counter.count(result)

        # Calculate total visible vehicles
        total_vehicles = sum(counts.values())

        # Draw YOLO bounding boxes
        annotated_frame = result.plot()

        # Create text to display
        text = (
            f"Total: {total_vehicles} | "
            f"Cars: {counts['car']} | "
            f"Motorcycles: {counts['motorcycle']} | "
            f"Buses: {counts['bus']} | "
            f"Trucks: {counts['truck']}"
        )

        # Display the count on the frame
        cv2.putText(
            annotated_frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        # Display the processed frame
        cv2.imshow(
            "AI Traffic Police - Vehicle Detection",
            annotated_frame
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = "../data/videos/traffic.MOV"
    process_video(video_path)
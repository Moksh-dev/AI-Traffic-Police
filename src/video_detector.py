import cv2

from detector import VehicleDetector


def process_video(video_path):
    detector = VehicleDetector()

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    print("Video opened successfully!")

    while True:
        success, frame = cap.read()

        if not success:
            break

        results = detector.model(frame)

        annotated_frame = results[0].plot()

        cv2.imshow("AI Traffic Police - Vehicle Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = "../data/videos/traffic.MOV"
    process_video(video_path)
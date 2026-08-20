# 🚦 AI Traffic Police

An AI-powered computer vision system for detecting, classifying, and counting vehicles from traffic images and videos.

The system uses a pre-trained YOLO model together with OpenCV to identify vehicles in traffic scenes and classify them into four categories:

- 🚗 Car
- 🏍️ Motorcycle
- 🚌 Bus
- 🚛 Truck

The application supports both image and video input through a single command-line interface and automatically saves processed results.

---

# 📌 Project Overview

AI Traffic Police is a computer vision-based application designed to analyse traffic images and videos.

Given an image or video, the system automatically:

1. Detects objects using a pre-trained YOLO model.
2. Filters detections to supported vehicle categories.
3. Classifies vehicles as cars, motorcycles, buses, or trucks.
4. Counts the detected vehicles.
5. Displays bounding boxes and labels.
6. Saves the processed image or video.

The application supports dynamic input, meaning a user can provide any supported image or video file without modifying the source code.

---

# ❗ Problem Statement

Manual traffic monitoring can be time-consuming and difficult to scale across large numbers of roads and surveillance cameras.

The objective of this project is to build an AI-based traffic analysis system capable of automatically detecting and classifying vehicles from images and videos.

For Part 1, the system focuses on:

- Vehicle detection
- Vehicle classification
- Vehicle counting from images
- Vehicle counting from videos

The supported vehicle categories are:

| Vehicle Type |
|---|
| Car |
| Motorcycle |
| Bus |
| Truck |

---

# ✨ Features

- 🖼️ Vehicle detection from images
- 🎥 Vehicle detection from videos
- 🚗 Car classification
- 🏍️ Motorcycle classification
- 🚌 Bus classification
- 🚛 Truck classification
- 🔢 Vehicle counting
- 📊 Frame-level vehicle counts for videos
- 📦 Dynamic image and video input
- 💾 Automatic processed image saving
- 🎬 Automatic processed video saving
- 🧠 Pre-trained YOLO model for object detection
- ⚡ Command-line interface

---

# 🏗️ Methodology

The system follows the pipeline below:

```text
                 INPUT IMAGE / VIDEO
                          │
                          ▼
                      main.py
                          │
                          ▼
                Detect Input Type
                    │         │
                    │         │
                 IMAGE      VIDEO
                    │         │
                    ▼         ▼
              Image Pipeline  Video Pipeline
                    │         │
                    └────┬────┘
                         │
                         ▼
                 VehicleDetector
                         │
                         ▼
                    YOLO Model
                         │
                         ▼
              Vehicle Class Filtering
                         │
                         ▼
             Car / Motorcycle / Bus / Truck
                         │
                         ▼
                  VehicleCounter
                         │
                         ▼
             Classification + Counting
                         │
                         ▼
                Display + Save Output
```

## Image Processing

For an input image:

```text
Image
  ↓
YOLO Detection
  ↓
Vehicle Filtering
  ↓
Classification
  ↓
Counting
  ↓
Annotated Image
  ↓
Save Result
```

## Video Processing

For an input video:

```text
Video
  ↓
OpenCV VideoCapture
  ↓
Read Frame
  ↓
YOLO Detection
  ↓
Vehicle Filtering
  ↓
Classification + Counting
  ↓
Annotate Frame
  ↓
Write Processed Frame
  ↓
Processed Video
```

Each video frame is processed independently.

---

# 🚗 Vehicle Classes

The pre-trained YOLO model uses COCO class IDs.

The system filters detections to the following vehicle classes:

| Vehicle | COCO Class ID |
|---|---:|
| Car | 2 |
| Motorcycle | 3 |
| Bus | 5 |
| Truck | 7 |

Only these classes are included in the vehicle counting process.

---

# 📂 Project Structure

```text
AI-Traffic-Police/
│
├── data/
│   ├── images/
│   │   └── traffic.jpg
│   │
│   └── videos/
│       └── traffic.MOV
│
├── experiments/
│   └── initial_detection_scripts/
│
├── outputs/
│   ├── images/
│   └── videos/
│
├── src/
│   ├── detector.py
│   ├── vehicle_counter.py
│   ├── video_detector.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 📊 Dataset Used

The project uses vehicle datasets downloaded from Roboflow for experimentation and testing.

Two datasets were explored:

### 1. Vehicles Dataset

- Source: Roboflow
- Format: Multi-Class Classification
- Approximate number of images: 4,549
- Classes include:
  - Bus
  - Motorcycle
  - Car
  - Truck

### 2. Vehicles-COCO Dataset

- Source: Roboflow
- Format: Multi-Class Classification
- Approximate number of images: 18,998
- Used for experimentation and testing with traffic and vehicle images.

The datasets were primarily used to explore the available vehicle classes and test the pre-trained detection pipeline.

The final implementation uses a pre-trained YOLO model for vehicle detection rather than training a custom model from scratch.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Ultralytics YOLO | Object detection |
| OpenCV | Image and video processing |
| NumPy | Image/frame data handling |
| Git | Version control |
| GitHub | Project hosting and submission |

---

# ⚙️ Installation Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Traffic-Police.git
```

Move into the project directory:

```bash
cd AI-Traffic-Police
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

The application accepts both images and videos using the `--source` argument.

General command:

```bash
python src/main.py --source "path_to_file"
```

---

## 🖼️ Run with an Image

Example:

```bash
python src/main.py --source "data/images/traffic.jpg"
```

The system will:

- Detect vehicles
- Classify vehicles
- Count each vehicle category
- Display results in the terminal
- Save the annotated image

Example terminal output:

```text
============================================================
                    AI TRAFFIC POLICE
             Vehicle Detection & Classification
============================================================

Processing image...

VEHICLE COUNT RESULTS
------------------------------------------------------------
Cars:        2
Motorcycles: 0
Buses:       1
Trucks:      0
------------------------------------------------------------
TOTAL VEHICLES: 3
============================================================

Detection completed successfully!
```

The processed image is saved inside:

```text
outputs/images/
```

---

## 🎥 Run with a Video

Example:

```bash
python src/main.py --source "data/videos/traffic.MOV"
```

The system will:

- Read the video frame by frame
- Detect supported vehicles
- Draw bounding boxes
- Display vehicle classes
- Display the number of vehicles visible in the current frame
- Save the processed video

The processed video is saved inside:

```text
outputs/videos/
```

---

# 📈 Results

The system successfully performs vehicle detection and classification on both images and videos.

### Image Results

The application successfully:

- Detects supported vehicles in an image.
- Filters detections to cars, motorcycles, buses, and trucks.
- Counts the number of detected vehicles.
- Generates and saves an annotated output image.

### Video Results

The application successfully:

- Processes videos frame by frame.
- Detects supported vehicle categories.
- Displays bounding boxes and class labels.
- Calculates vehicle counts for each frame.
- Saves the processed video.

Example frame-level output:

```text
Total: 8 | Cars: 5 | Motorcycles: 1 | Buses: 1 | Trucks: 1
```

> Vehicle counts in videos represent the vehicles visible in the current frame.

---

# 📸 Screenshots

## Image Detection Result

> Add your actual processed image here.

```md
![Image Detection Result](assets/image_result.png)
```

## Video Detection Result

> Add a screenshot captured from the processed video here.

```md
![Video Detection Result](assets/video_result.png)
```

The `assets` folder can contain screenshots used in this README:

```text
assets/
├── image_result.png
└── video_result.png
```

---

# ⚠️ Challenges Faced

Several challenges were encountered during the development process.

### 1. Dataset Format

The downloaded vehicle datasets were exported in Multi-Class Classification format. This required understanding the difference between image classification datasets and object detection datasets with bounding-box annotations.

### 2. Model Path and Download Issues

The YOLO model initially attempted to download automatically, but network connection issues caused download failures. This was resolved by using the locally available model file.

### 3. File Path Handling

Different parts of the application initially used hardcoded file paths. The system was later improved to accept dynamic image or video paths using command-line arguments.

### 4. Synchronizing Components

As the project architecture evolved, methods in different files became inconsistent. For example, the vehicle counting interface required synchronization with the main application pipeline.

### 5. Video Output Generation

Saving processed videos required preserving the input video's frame dimensions and frame rate while writing annotated frames into a new output file.

---

# 🔮 Future Improvements

Possible improvements include:

- Object tracking across video frames.
- Unique vehicle counting.
- Vehicle speed estimation.
- Traffic density analysis.
- Congestion detection.
- Lane detection.
- Number plate recognition.
- Traffic violation detection.
- Real-time CCTV or webcam integration.
- Traffic analytics dashboard.
- Fine-tuning a pre-trained model on a traffic-specific object detection dataset.

---

# 🧠 Key Learning

This project demonstrates a practical computer vision pipeline using a pre-trained object detection model.

A key distinction explored during development was:

### Object Detection

Object detection identifies objects independently in an image or video frame.

Example:

```text
Frame
├── Car
├── Car
└── Bus
```

### Object Tracking

Object tracking would associate the same detected object across consecutive frames.

Example:

```text
Frame 1 → Car ID 1
Frame 2 → Car ID 1
Frame 3 → Car ID 1
```

The current implementation focuses on object detection and frame-level counting. Object tracking is identified as a future improvement.

---

# 👩‍💻 Author

**Kashish Goel**

B.Tech Computer Science Engineering  
Specialization: Artificial Intelligence and Machine Learning

---

## ⭐ Project Status

**Part 1 – Vehicle Classification and Counting: Completed**

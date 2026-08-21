# 🚦 AI Traffic Police

An AI-powered vehicle detection and counting system built using **Python, Ultralytics YOLO, and OpenCV**.

The system accepts both **images and videos**, detects vehicles, filters relevant traffic classes, counts them, and saves annotated outputs. It also includes an inference-based evaluation pipeline using the provided vehicle datasets.

---

## 📌 Project Overview

AI Traffic Police is a computer vision project designed to detect and count vehicles from traffic images and videos.

The system uses a **pre-trained YOLO model** for object detection and focuses on four vehicle categories:

- 🚗 Car
- 🏍️ Motorcycle
- 🚌 Bus
- 🚚 Truck

The application supports dynamic input, meaning users can provide their own image or video without modifying the source code.

---

## 🎯 Problem Statement

Traffic monitoring often requires manually analysing large amounts of image or video data.

The goal of this project is to build a reusable computer vision pipeline that can:

- Detect vehicles from traffic images.
- Process traffic videos frame by frame.
- Identify relevant vehicle categories.
- Count detected vehicles.
- Generate annotated output images and videos.
- Evaluate the detection pipeline using the provided datasets.

---

## ✨ Features

- Vehicle detection using a pre-trained YOLO model.
- Supports both images and videos.
- Dynamic input through the `--source` command-line argument.
- Detection of cars, motorcycles, buses, and trucks.
- Frame-level vehicle counting for videos.
- Annotated image output.
- Annotated video output.
- Dataset evaluation pipeline.
- CSV evaluation reports.
- Modular project structure.

---

# 🏗️ Project Architecture

```text
                IMAGE / VIDEO
                      │
                      ▼
                 main.py
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
      Image Input              Video Input
          │                       │
          ▼                       ▼
    VehicleDetector         VideoDetector
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
              Pre-trained YOLO
                      │
                      ▼
              Object Detection
                      │
                      ▼
              Vehicle Filtering
                      │
                      ▼
              VehicleCounter
                      │
                      ▼
             Annotated Output
```

---

# 📁 Project Structure

```text
AI-Traffic-Police/
│
├── assets/
│
├── data/
│   ├── images/
│   └── videos/
│
├── docs/
│
├── experiments/
│
├── models/
│   └── yolo26n.pt
│
├── outputs/
│   ├── images/
│   ├── videos/
│   └── evaluation/
│
├── src/
│   ├── detector.py
│   ├── vehicle_counter.py
│   ├── video_detector.py
│   ├── dataset_evaluator.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation Instructions

## 1. Clone the repository

```bash
git clone https://github.com/Moksh-dev/AI-Traffic-Police.git
```

Move into the project directory:

```bash
cd AI-Traffic-Police
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

## Run on an image

```bash
python src/main.py --source "data/images/traffic.jpg"
```

The image does not have to be inside the project.

For example:

```bash
python src/main.py --source "C:\Users\YourName\Downloads\traffic.jpg"
```

## Run on a video

```bash
python src/main.py --source "data/videos/traffic.MOV"
```

You can also provide an external video:

```bash
python src/main.py --source "C:\Users\YourName\Downloads\traffic.mp4"
```

---

# 🧠 Methodology

The project uses a modular computer vision pipeline.

## Step 1: Input Detection

The user provides an image or video using the `--source` argument.

`main.py` determines whether the source is an image or video and routes it to the appropriate processing pipeline.

## Step 2: YOLO Object Detection

The pre-trained YOLO model processes the input and produces predictions containing:

- Bounding boxes
- Class IDs
- Confidence scores

## Step 3: Vehicle Filtering

YOLO can detect multiple object categories.

This project filters predictions to the following vehicle classes:

```text
Car
Motorcycle
Bus
Truck
```

Non-vehicle detections are ignored.

## Step 4: Vehicle Counting

The filtered detections are passed to `VehicleCounter`.

For images, the detected vehicles are counted once.

For videos, the system performs **frame-level counting**, meaning the displayed count represents vehicles detected in the current frame.

## Step 5: Output Generation

The system generates annotated outputs containing:

- Vehicle bounding boxes
- Vehicle class labels
- Vehicle counts

Processed files are saved inside the `outputs/` directory.

---

# 📊 Dataset Used

The project uses the following provided datasets for evaluation:

### Dataset 1

```text
Vehicles-coco.v2i.multiclass
```

### Dataset 2

```text
Vehicles.v1i.multiclass
```

These datasets were used as **evaluation inputs**.

The pre-trained YOLO model was **not retrained or fine-tuned** using these datasets.

The evaluation pipeline processes each image and records detection statistics.

---

# 📈 Evaluation Methodology

The dataset evaluation process follows this pipeline:

```text
Dataset Folder
      │
      ▼
Find All Images
      │
      ▼
YOLO Inference
      │
      ▼
Vehicle Filtering
      │
      ▼
Vehicle Counting
      │
      ▼
Aggregate Statistics
      │
      ▼
CSV Evaluation Report
```

The evaluation reports include:

- Number of images processed.
- Images with at least one supported vehicle detected.
- Vehicle detection rate.
- Cars detected.
- Motorcycles detected.
- Buses detected.
- Trucks detected.
- Total vehicle detections.
- Average vehicles detected per image.

> **Note:** The reported vehicle detection rate is not the same as model accuracy. It represents the percentage of processed images in which the system detected at least one supported vehicle class.

---

# 📊 Results

## Vehicles-COCO Dataset

| Metric | Result |
|---|---:|
| Images Processed | 13,300 |
| Images with Vehicles Detected | 9,474 |
| Vehicle Detection Rate | 71.23% |
| Cars Detected | 11,901 |
| Motorcycles Detected | 2,779 |
| Buses Detected | 3,196 |
| Trucks Detected | 2,592 |
| Total Vehicle Detections | 20,468 |
| Average Vehicles per Image | 1.54 |

---

## Vehicles Dataset

| Metric | Result |
|---|---:|
| Images Processed | 4,311 |
| Images with Vehicles Detected | 512 |
| Vehicle Detection Rate | 11.88% |
| Cars Detected | 242 |
| Motorcycles Detected | 10 |
| Buses Detected | 127 |
| Trucks Detected | 300 |
| Total Vehicle Detections | 679 |
| Average Vehicles per Image | 0.16 |

The difference in results demonstrates that the performance of a pre-trained detection pipeline can vary depending on the characteristics and distribution of the input data.

---

# 🛠️ Technologies Used

- Python
- Ultralytics YOLO
- OpenCV
- PyTorch
- Git
- GitHub

---

# 📦 Requirements

All project dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# ⚠️ Challenges Faced

## 1. Dynamic File Handling

Initially, the system relied on fixed file paths.

This was improved by adding support for:

```bash
--source
```

This allows users to provide any supported image or video.

## 2. Separating Detection and Counting

Instead of placing all logic in one script, the system was separated into modules responsible for:

- Detection
- Vehicle filtering
- Counting
- Video processing
- Dataset evaluation

This improves code readability and maintainability.

## 3. Video Processing

Videos require frame-by-frame processing.

OpenCV is used to:

- Read video frames.
- Process each frame using YOLO.
- Annotate detections.
- Save the processed video.

## 4. Dataset Evaluation

The provided datasets were used for inference-based evaluation.

Because the current pipeline does not compare predictions against bounding-box ground truth, traditional object detection metrics such as mAP and IoU are not reported.

Instead, the project reports transparent inference statistics.

---

# 🔮 Future Improvements

Possible future improvements include:

- Object tracking for unique vehicle counting.
- Traffic density analysis.
- Congestion detection.
- Real-time webcam or CCTV support.
- Custom model training using bounding-box annotated traffic data.
- A web-based dashboard for visualising traffic statistics.

---

# 📸 Screenshots

## Image Detection

![Image Detection](assets/image_result.png)

## Video Detection

![Video Detection](assets/video_result.png)

## Dataset Evaluation

![Dataset Evaluation](assets/dataset_evaluation.png)

---

# 🎥 Demo

The project can be demonstrated using:

### Image Detection

```bash
python src/main.py --source "data/images/traffic.jpg"
```

### External Image Detection

```bash
python src/main.py --source "C:\Users\YourName\Downloads\test.jpg"
```

### Video Detection

```bash
python src/main.py --source "data/videos/traffic.MOV"
```

### Dataset Evaluation

```bash
python src/dataset_evaluator.py --dataset "datasets/Vehicles-coco.v2i.multiclass/train"
```

---

# 📌 Limitations

The current video implementation performs **frame-level vehicle counting**.

This means the same vehicle may be detected in multiple consecutive frames.

The current project does not yet perform object tracking or unique vehicle identification across an entire video.

---

# 📄 Project Status

## Part 1 — Vehicle Detection and Frame-Level Counting

**Completed ✅**

The current implementation provides:

- Image detection
- Video detection
- Vehicle filtering
- Frame-level counting
- Dynamic source handling
- Annotated output saving
- Dataset evaluation
- CSV evaluation reports

The project was developed using an incremental Git commit history to document the evolution of the system.
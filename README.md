# 🚦 AI Traffic Police

> An AI-powered vehicle detection, classification, and counting system built using YOLO and OpenCV.

AI Traffic Police processes traffic images and videos to detect vehicles, classify them into supported vehicle categories, and provide real-time frame-level counts.

---

## ✨ Features

- 🚗 Detect vehicles from images
- 🎥 Process traffic videos frame by frame
- 🚌 Classify supported vehicle types:
  - Car
  - Motorcycle
  - Bus
  - Truck
- 🔢 Count vehicles visible in each frame
- 📦 Accept both images and videos as dynamic input
- 🖼️ Save processed images automatically
- 🎬 Save processed videos automatically
- 🧠 Uses a pre-trained YOLO model for object detection
- ⚡ Simple command-line interface

---

## 🏗️ Project Architecture

```text
                    INPUT
                      │
          ┌───────────┴───────────┐
          │                       │
        IMAGE                   VIDEO
          │                       │
          └───────────┬───────────┘
                      ↓
                 main.py
                      ↓
             Detect source type
                      ↓
          ┌───────────┴───────────┐
          │                       │
    Image Pipeline           Video Pipeline
          │                       │
          └───────────┬───────────┘
                      ↓
               VehicleDetector
                      ↓
               YOLO Inference
                      ↓
        Filter Vehicle Classes
                      ↓
               VehicleCounter
                      ↓
        Classification + Counting
                      ↓
          Display + Save Results

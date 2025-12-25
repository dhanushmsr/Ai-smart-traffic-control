# Ai-smart-traffic-control
# 🚦 AI-Based Smart Traffic Management System

An intelligent real-time traffic monitoring and signal control system using **Artificial Intelligence**, **Computer Vision**, and **Web Technologies**.  
This system dynamically adjusts traffic signals based on vehicle density and gives **priority to emergency vehicles** with **voice and sound alerts**.

---

## 📌 Features

- 🎥 **Live Camera & Video Upload Monitoring**
- 🚗 **Vehicle Detection & Counting (Cars, Bikes, Buses, Trucks)**
- 🚑 **Emergency Vehicle Detection (Ambulance Priority)**
- 🚦 **Dynamic Traffic Signal Control**
- 🔊 **Female AI Voice Alerts (Chrome Supported)**
- 🚨 **Emergency Siren Alert System**
- 📊 **Live Traffic Dashboard**
- 🎨 **Modern Glassmorphism UI**
- ⚡ **Real-Time Traffic Density Analysis**

---

## 🧠 Technologies Used

### Backend
- Python
- Flask
- OpenCV
- YOLO (Object Detection)
- NumPy

### Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- JavaScript
- Web Speech API (Text-to-Speech)

### Tools
- VS Code
- Chrome Browser
- Git & GitHub

---



## 🚦 Traffic Signal Logic

| Traffic Level | Signal | Green Time |
|--------------|--------|------------|
| LOW          | 🟢 Green | 60 sec     |
| MEDIUM       | 🟡 Yellow| 40 sec     |
| HIGH         | 🔴 Red   | 20 sec     |
| EMERGENCY    | 🔴 Red   | Priority   |

---

## 🔊 Voice Alert System

- Uses **Female AI Voice**
- Triggered only after **user interaction**
- Alerts include:
  - Emergency vehicle detected
  - Signal cleared for ambulance

> Note: Chrome browser requires user click to enable voice alerts.

---

## 🖥️ User Interface Overview

- Control Panel (Live / Upload Mode)
- Traffic Signal Visualization
- Real-Time Statistics Cards
- Emergency Alert Indicator
- Voice Alert Enable Button

---


### Step 1: Clone Repository
```bash
git clone https://github.com/dhanushmsr/ai-smart-traffic-control
cd ai-smart-traffic-control
project/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── sounds/
│   └── videos/
├── models/
│   └── yolo.weights
├── requirements.txt
└── README.md

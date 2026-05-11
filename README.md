# 🚍 TransitGuard AI - Smart Transit Alert System

**TransitGuard AI** is a location-aware web application designed for commuters using public transport. It uses real-time GPS tracking to monitor your journey and triggers an alarm when you are about to reach your destination, ensuring you never miss your stop.

---

## ✨ Features

- **Real-time Geofencing:** Continuous monitoring of live GPS coordinates.
- **AI-based ETA Prediction:** Calculates Estimated Time of Arrival based on distance and average speed.
- **Proximity Alarm:** Automatically plays an alert sound when you enter the pre-set radius.
- **Modern Dark UI:** Responsive and sleek interface for mobile and desktop users.
- **Customizable Alerts:** Users can set their own destination and alarm radius.
<img width="800" height="300" alt="image" src="https://github.com/user-attachments/assets/b4fc5dc9-a117-49d3-aed2-bbbe86ca3e0f" />

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (Geolocation API)
- **Backend:** Python (Flask Framework)
- **Communication:** AJAX/JSON for real-time updates
- **Logic:** Distance-based predictive algorithms

---

## 🚀 Installation & Setup

### 1. Clone the Project
```bash
git clone [https://github.com/your-username/TransitGuard-AI.git](https://github.com/your-username/TransitGuard-AI.git)
cd TransitGuard-AI

```

### 2. Install Flask

```bash
pip install flask

```

### 3. Run the Application

```bash
python app.py

```

### 4. Access in Browser

Open: `http://127.0.0.1:5000`

---

## 📝 How to Use

1. **Location Access:** Click **Allow** when the browser asks for location permissions.
2. **Set Destination:** Enter the **Latitude** and **Longitude** of your target stop.
3. **Set Radius:** Input the distance in kilometers (e.g., 0.5 for 500 meters) for the alarm.
4. **Activate:** Click **START MONITORING**.
5. **Alert:** The system will update distance in real-time and sound the alarm once you enter the radius.

---

## 📌 Important Notes

* Works best on mobile devices with high-accuracy GPS enabled.
* Ensure `alert.mp3` is present in the `static` folder for the alarm to function.
* Browser policy requires one user interaction (click) to enable audio playback.

---

## 👨‍💻 Contributor

* **Sanika Gundakar** -


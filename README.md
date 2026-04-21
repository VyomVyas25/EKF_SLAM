# EKF-SLAM (ROS 2 Humble)

Extended Kalman Filter (EKF) based **Simultaneous Localization and Mapping (SLAM)** implemented in **ROS 2 Humble**.  
This project integrates **odometry + LiDAR measurements** to estimate robot pose and landmark positions in the environment.  
Visualization in RViz2 shows the robot trajectory and detected landmarks in real-time.

---

## 📂 Workspace Structure

```
ekf_slam_ws
└── src
    └── ekf_slam_pkg
        ├── ekf_slam_pkg
        │   ├── EKF_slam.py       # Main EKF-SLAM node
        │   ├── viz_ekf_slam.py   # Visualization node (path + landmarks)
        │   └── __init__.py
        ├── package.xml
        └── setup.py
```

---

## 🚀 Features

- **EKF Prediction + Correction** using odometry and LiDAR.
- **Landmark detection** and dynamic augmentation of state vector.
- **Data association** for re-observed landmarks.
- **Visualization** in RViz2:
  - Robot trajectory (`/slam_path`)
  - Landmarks (`/slam_landmarks`) as cylinders.

---

## ⚙️ Requirements

- ROS 2 Humble
- Python 3.10+
- Dependencies (already in `package.xml`):
  - `rclpy`
  - `geometry_msgs`
  - `nav_msgs`
  - `sensor_msgs`
  - `std_msgs`
  - `visualization_msgs`
  - `tf_transformations`
  - `numpy`

---

## 🛠️ Build Instructions

Clone the repo and build the workspace:

```bash
# Clone this repo
git clone https://github.com/VyomVyas25/EKF_SLAM.git
cd EKF_SLAM/ekf_slam_ws

# Build
colcon build

# Source
source install/setup.bash
```

---

## ▶️ Running

**1. Start the EKF-SLAM node**
```bash
ros2 run ekf_slam_pkg ekf_slam
```

**2. Start the visualization node**
```bash
ros2 run ekf_slam_pkg ekf_slam_viz
```

**3. Open RViz2**
```bash
rviz2
```

Set `Fixed Frame = odom` and add displays:
- `Path` → topic `/slam_path`
- `MarkerArray` → topic `/slam_landmarks`

---

## 📊 Results & Visualization

### 🔍 RViz2 — LiDAR Scan + 2D Goal Navigation
> The left panel shows the robot (top-down) with LiDAR scan rays (blue fan) actively sensing the environment. The right panel shows the Nav2 2D map with orange landmark markers and a planned path to the goal pose.

![RViz LiDAR Scan and 2D Goal Pose]([src/ekf_slam_pkg/Screenshot from 2026-04-21 14-30-34.png](https://github.com/VyomVyas25/EKF_SLAM/blob/main/src/ekf_slam_pkg/Screenshot%20from%202026-04-21%2014-30-34.png))

---

### 🗺️ EKF-SLAM — Full Loop Trajectory
> The robot successfully navigates a full loop around the environment. The **red line** represents the odometry-only estimate, while the **green line** shows the EKF-corrected trajectory. Orange cylinders are the detected and mapped landmarks.

![EKF SLAM Full Loop Trajectory](docs/images/ekf_slam_full_loop.png)

---

### 🤖 EKF-SLAM — Live Navigation with Path Tracking
> A closer view of the robot mid-navigation. The EKF-SLAM algorithm continuously corrects the robot's estimated pose using landmark observations, keeping the green (corrected) path tightly aligned with the true trajectory.

![EKF SLAM Live Navigation](docs/images/ekf_slam_navigation.png)

---

### Legend
| Color | Meaning |
|-------|---------|
| 🟢 Green path | EKF-corrected robot trajectory |
| 🔴 Red path   | Raw odometry estimate |
| 🟠 Orange cylinders | Detected & mapped landmarks |

---

## 📁 Adding Images to Your Repository

To display the screenshots above, place your images in the repo under:
```
docs/
└── images/
    ├── ekf_slam_rviz_lidar.png
    ├── ekf_slam_full_loop.png
    └── ekf_slam_navigation.png
```

Then push them:
```bash
git add docs/images/
git commit -m "Add EKF-SLAM result screenshots"
git push
```

---

## About

This repository contains self-developed packages and nodes for EKF-based SLAM algorithms in ROS2. The code is designed to be modular and extensible. SLAM integration is currently under development.

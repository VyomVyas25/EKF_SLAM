# EKF-SLAM (ROS 2 Humble)

Extended Kalman Filter (EKF) based **Simultaneous Localization and Mapping (SLAM)** implemented in **ROS 2 Humble**.  
This project integrates **odometry + LiDAR measurements** to estimate robot pose and landmark positions in the environment.  
Visualization in RViz2 shows the robot trajectory and detected landmarks in real-time.

---

## 📂 Workspace Structure
ekf_slam_ws/
└── src/
└── ekf_slam_pkg/
├── ekf_slam_pkg/
│ ├── EKF_slam.py # Main EKF-SLAM node
│ ├── viz_ekf_slam.py # Visualization node (path + landmarks)
│ └── init.py
├── package.xml
└── setup.py

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

# Clone this repo
```bash
git clone https://github.com/VyomVyas25/EKF_SLAM.git
cd EKF_SLAM/ekf_slam_ws
```

# Build
```bash
colcon build
```

# Source
```bash
source install/setup.bash
```
▶️ Running
1. Start the EKF-SLAM node
```bash
ros2 run ekf_slam_pkg ekf_slam
```

3. Start the visualization node
```bash
ros2 run ekf_slam_pkg ekf_slam_viz
```

5. Open RViz2
```bash
rviz2
```

Set Fixed Frame = odom

Add displays:

Path → topic /slam_path

MarkerArray → topic /slam_landmarks

📊 Example RViz View

Green line = robot path

Orange cylinders = detected landmarks

---


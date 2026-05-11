# AMR ROS2 Prototype | Hardware & Software Integration

This project is the development of an **Autonomous Mobile Robot (AMR)** prototype, serving as a foundational step toward mastering the systems engineering required for humanoid robotics.

## 🤖 System Overview
- **Middleware:** ROS2 (Humble/Jazzy).
- **Hardware Control:** Integrated **Arduino** for low-level motor actuation and sensor data processing.
- **Mechanical Design:** Chassis and component mounts designed in **Autodesk Inventor**.

## 📂 Repository Structure
- **/src**: Contains ROS2 packages for motor control, sensor fusion, and node communication.
- **.gitignore**: Configured to exclude build artifacts (`build/`, `install/`, `log/`), ensuring a clean source-only repository.

## 🚀 Current Status
- [x] Initial ROS2 node architecture completed.
- [x] Mechanical chassis design finalized in CAD.
- [ ] Physical fabrication and assembly. (In Progress)
- [ ] SLAM and Navigation stack integration. (Planned)

## 📈 Learning Goals
This project is an independent exercise in moving from "blindly following" tutorials to **Architecting Systems**. It focuses on mastering the foundational gears of robotics: message passing, hardware-software interfaces, and mechanical integrity.

**Project Mentor:** Prof. Sreedhar Madichetty (Mahindra University) 
**End Goal:** Design a mobile robot capable of autonomously carrying a **20kg payload**.

## 🛠️ Hardware Stack (Stages 1-4) 
- **Actuation:** 12V Planetary Gear DC Motors (72.5 N-cm, 185RPM) with encoders.
- **Processing:** Raspberry Pi 4 Model B (High-level) and Arduino MEGA2560 (Low-level).
- **Sensing:** SLAMTEC RPLIDAR A1M8 (360° Laser Range Finder) and HC-SR04 Ultrasonic Sensors.
- **Power:** 3S LiPo Battery (11.1V, 2200mAh) with Buck Converters for voltage regulation.

## 💻 Software & Middleware
- **OS:** Ubuntu 22.04 LTS & Windows 11.
- **Middleware:** ROS2 Humble with Nav2 Stack and SLAM Toolbox.
- **Simulation:** Gazebo and RViz2 for visualization.
- **Design:** Autodesk Inventor for mechanical architecture.

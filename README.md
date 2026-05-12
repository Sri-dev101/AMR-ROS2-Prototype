# AMR ROS2 Prototype | Hardware & Software Integration

This project is the development of an **Autonomous Mobile Robot (AMR)** prototype, serving as a foundational step toward mastering the systems engineering required for humanoid robotics.

**Project Mentor:** [Prof. Sreedhar Madichetty](https://www.linkedin.com/in/sreedhar-madichetty-71b6195a/)  
**Student Mentor:** [R V S Srikasyap Sagar](https://www.linkedin.com/in/r-v-s-srikasyap-sagar/)

## 🤖 System Overview
This project focuses on designing a mobile robot from the ground up, capable of carrying a **maximum payload of 20kg** from point A to point B autonomously. The objective is to move beyond theoretical study and gain real-world experience with ROS2, microcontrollers, and microprocessors.

## 🛠️ Hardware Stack
* **Actuation:** 12V Planetary Gear DC Motors (x4) with encoders (72.5 N-cm, 185RPM).
* **Motor Control:** BTS7960 Motor Drivers (x2) and Arduino MEGA2560.
* **Processing:** Raspberry Pi 4 Model B.
* **Sensing:** SLAMTEC RPLIDAR A1M8 (360° Laser Range Finder) and HC-SR04 Ultrasonic Sensors.
* **Weight Sensing:** Load Cells (x4, 50kg) with HX711 24-Bit Amplifiers.
* **Power:** 3S Lithium Polymer (LiPo) Battery (11.1V, 2200mAh) with LM2596S DC-DC Buck Converter.

## 💻 Software & Middleware
* **Operating Systems:** Ubuntu 22.04 LTS and Windows 11.
* **Middleware:** ROS2 Humble with Nav2 Stack and SLAM Toolbox.
* **Firmware:** Arduino IDE and Micro-ROS.
* **Design Tools:** Autodesk Inventor, Cirkit designer IDE, and Tinkercad.
* **Simulation:** Gazebo and RViz2.

## 🗺️ Roadmap

### Stage 1: The Hardware MVP
* Comprehensive circuit and mechanical design.
* Chassis fabrication, assembly, and wiring.
* Initial system integration and low-level programming.

### Stage 2: The Digital Twin
* Spatial frame architecture and kinematic modeling.
* Dynamic state broadcasting and parametric model optimization.
* Physics engine integration for simulation accuracy.

### Stage 3: The Brain Transplant
* Microcomputer (Raspberry Pi) environment provisioning.
* Serial UART bridge implementation and kinematic odometry publishing.
* Velocity command subscription and closed-loop teleoperation validation.

### Stage 4: Autonomy & Perception
* Probabilistic SLAM and Map Generation.
* Custom environment simulation and fine-tuning.
* Autonomous path planning validation and hardware Nav2 integration.

## 📂 Repository Structure
* **/src**: ROS2 packages and Python nodes for robot logic.
* **/hardware_cad**: Autodesk Inventor (.ipt, .iam) models and circuit schematics.
* **.gitignore**: Configured to exclude build, install, and log artifacts.

## 📈 Learning Goals
My primary motivation is to utilize hands-on learning to understand robotics from the ground up. By building this robot from scratch-designing hardware, wiring electronics, and writing code - I am mastering the foundational gears of autonomous systems.

## 🙏 Acknowledgments
Special thanks to the following individuals for their technical guidance:

* **[Prof.Sreedhar Madichetty](https://www.linkedin.com/in/sreedhar-madichetty-71b6195a/)**: For project oversight and academic mentorship.
* **[R V S Srikasyap Sagar](https://www.linkedin.com/in/r-v-s-srikasyap-sagar/)**: For coordinating mechatronics and software integration.
* **[Arvind Prabhu](https://www.linkedin.com/in/arvind-prabhu-50411031b/)**: For providing expert mentorship in **Autodesk Inventor** and mechanical architecture optimization.

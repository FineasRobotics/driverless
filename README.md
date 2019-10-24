
jCricket is Pinokio's Soul & Brain, the software running behind Fineas's 1st fully autonomous race car.

### Setup(Ubuntu 16.04, ROS Kinetic)
1. Install packages `sudo apt-get install ros-kinetic-gazebo-ros-control ros-kinetic-ros-controllers ros-kinetic-navigation ros-kinetic-gmapping ros-kinetic-teb-local-planner ros-kinetic-robot-localization ros-kinetic-robot-pose-ekf ros-kinetic-ackermann-msgs ros-kinetic-twist-mux ros-kinetic-controller-manager ros-kinetic-robotnik-msgs ros-kinetic-velodyne-simulator`
2. Create a new catkin workspace if you don't have one already.
3. To clone the files directly (without an extra folder), run inside the src folder:
    - `git init`
    - `git remote add origin https://gitlab.com/fineasracingteam/jcricket.git`
    - `git fetch --all`
    - `git pull origin master`
4. Run `catkin_make`.

### How to run
1. Source the workspace(`source devel/setup.bash` or check our [ROS Basics](https://docs.google.com/document/d/1HTMq7Cwe4MZPlNUSJqRnfYy1TClEv3lscJfn8Ei_yrE/edit?usp=sharing) doc for more information).
2. Run: `roslaunch simulation gazebo_simulation.launch`.
Tip: you can make gazebo open its GUI by changing gui argument inside gazebo_simulation.launch file to true.

### Send a goal using RViz
Press 2D Nav Goal, hold it in the spot you want to send the goal, and turn it to the direction you want your robot to have when it reaches the goal.

### Send a goal using move_base_sequence
Use argument goal_seq when launching: `roslaunch simulation gazebo_simulation.launch goal_seq:=true`.   
For more information on how it works and how to modify the goal sequence check [control readme](3_control/robot_control/README.md).

### Control the robot using rqt
Use argument manual_control when launching: `roslaunch simulation gazebo_simulation.launch manual_control:=true`.

### Control the robot with the keyboard
Open another terminal and run: `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

### Workspace Structure
    ├── 0_frt_common
    │   └── simulation
    │       ├── launch
    │       ├── rviz
    │       └── worlds
    ├── 1_perception
    │   └── perception_common
    ├── 2_estimation
    │   ├── cone_global_planner
    │   └── estimation_common
    └── 3_control
        ├── eufs_description
        └── robot_control

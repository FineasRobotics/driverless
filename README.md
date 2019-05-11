
jCricket is Pinokio's Soul & Brain, the software running behind Fineas's 1st fully autonomous race car.

### Setup
1. Install packages `sudo apt-get install ros-kinetic-gazebo-ros-pkgs ros-kinetic-gazebo-ros-control ros-kinetic-navigation ros-kinetic-sbpl ros-kinetic-pose-follower ros-kinetic-teleop-twist-keyboard`
2. Create a new catkin workspace if you don't have one already.
3. Clone this repository inside your workspace/src folder.
4. Run `catkin_make`.

### How to run
1. Source the workspace.
2. Run: `roslaunch simulation gazebo_simulation.launch`

### Send a goal using RViz
Press 2D Nav Goal , hold it in the spot you want to send the goal, and turn it to the direction you want your robot to have when it reaches the goal.

### Control the robot with the keyboard
Open another terminal and run: `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

### Workspace Structure
    ├── 0_frt_common
    │   ├── robot
    │   │   ├── meshes
    │   │   └── urdf
    │   └── simulation
    │       ├── launch
    │       ├── rviz
    │       └── worlds
    ├── 1_perception
    ├── 2_estimation
    │   ├── estimation_common
    │   │   ├── config
    │   │   ├── launch
    │   │   └── script
    │   └── sbpl_lattice_planner
    └── 3_control

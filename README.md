
jCricket is Pinokio's Soul & Brain, the software running behind Fineas's 1st fully autonomous race car.

### Setup(For Ubuntu 16.04)
1. Install packages `sudo apt-get install ros-kinetic-gazebo-ros-control ros-kinetic-ros-controllers ros-kinetic-navigation ros-kinetic-gmapping ros-kinetic-teb-local-planner`
2. Create a new catkin workspace if you don't have one already.
3. Clone this repository inside your workspace/src folder.
   To clone the files directly inside the src folder(without an extra folder), run inside the src folder:
    - git init
    - git remote add origin https://gitlab.com/fineasracingteam/jcricket.git (or git@gitlab.com:fineasracingteam/jcricket.git if you have an SSH key)
    - git fetch --all (to get all the branches)
    - git pull origin master 
4. Run `catkin_make`.

### How to run
1. Source the workspace.
2. Run: `roslaunch simulation gazebo_simulation.launch`
3. if the robot doesnt robot doesnt show up use rosrun car_description tf_robot_odom_bridge.py

### Send a goal using RViz
Press 2D Nav Goal , hold it in the spot you want to send the goal, and turn it to the direction you want your robot to have when it reaches the goal.

### Control the robot with the keyboard
Open another terminal and run: `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

### Workspace Structure
    ├── 0_frt_common
    │   ├── robot
    │   └── simulation
    │       ├── launch
    │       ├── rviz
    │       └── worlds
    ├── 1_perception
    ├── 2_estimation
    │   ├── cone_global_planner
    │   └── estimation_common
    └── 3_control
        └── car_description


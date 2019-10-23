
jCricket is Pinokio's Soul & Brain, the software running behind Fineas's 1st fully autonomous race car.

### Setup(For Ubuntu 16.04)
1. Install packages `sudo apt-get install ros-kinetic-gazebo-ros-control ros-kinetic-ros-controllers ros-kinetic-navigation ros-kinetic-gmapping ros-kinetic-teb-local-planner ros-kinetic-robot-localization ros-kinetic-robot-pose-ekf ros-kinetic-ackermann-msgs ros-kinetic-twist-mux ros-kinetic-controller-manager ros-kinetic-robotnik-msgs ros-kinetic-velodyne-simulator`
2. Create a new catkin workspace if you don't have one already.
3. To clone the files directly (without an extra folder), run inside the src folder:
    - git init
    - git remote add origin https://gitlab.com/fineasracingteam/jcricket.git (or git@gitlab.com:fineasracingteam/jcricket.git if you have an SSH key)
    - git fetch --all (to get all the branches)
    - git pull origin master 
4. Run `catkin_make`.

### How to run
1. Source the workspace.
2. Run: `roslaunch simulation gazebo_simulation.launch model:=car` or robot.

### Send a goal using RViz
Press 2D Nav Goal, hold it in the spot you want to send the goal, and turn it to the direction you want your robot to have when it reaches the goal.

### Send a goal using move_base_sequence
Launch `move_base_seq.py` using the `movebase_seq.launch file`. `Move_base_seq` is generating a goal sequence based on the paramatered goals defined in the `movebase_seq.launch` file. To incorporate a goal to the goal sequence add it's cartesian coordinates(x,y,z) into the `p_seq` rosparam seperated by a comma and it's yaw angle into the `yea_seq` param. For each yaw angle in `yea_seq` `move_base_seq` requires a set of coordinates in the `p_seq` so that `p_seq`[i], `yea_seq`[i].


### Control the robot using rqt
Use argument manual_control during launch: `roslaunch simulation gazebo_simulation.launch model:=car manual_control:=true`.

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
    │   └── perception_common
    ├── 2_estimation
    │   ├── cone_global_planner
    │   └── estimation_common
    └── 3_control
        ├── eufs_description
        └── robot_control

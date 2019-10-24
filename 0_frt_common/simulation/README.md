# simulation
Contains the RViz configuration, the world files, the launch files and movebase_seq for the simulation with Gazebo.

## Nodes
* `move_base_seq.py` - generates a goal sequence based on the goals listed in the `movebase_seq.launch` file

To add a goal to the goal sequence:
  - add it's cartesian coordinates(x,y,z) into the `p_seq` rosparam seperated by a comma 
  - add it's yaw angle into the `yea_seq` param.
Those go in pairs, so always add/delete from both.

## Launch files
* `gazebo_simulation.launch` - launches gazebo, rviz and everything else that is needed for our simulation.
* `movebase_seq.launch` - launches a series of goals listed in the launch file.


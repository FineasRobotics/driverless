## Package: estimation_common
It contains the config files(.yaml) that the costmaps, planners and SLAM use.
It also contains the launch file for costmaps, planners and SLAM.

## Library-Global Planner: cone_global_planner
WIP - Contains an dummy version of our custom global planner in C++ and the 
logic in python scripts.
What it **will** do:
- Get cone information from the sensors.
- Order the points so they can form a line. - See point_sorter.py
- Remove outliers. - See outlier_remover.py WIP
- Calculate the middle line between the lines that the cones create. - See middle_line_finder.py
- Publish that path.

cmake_minimum_required(VERSION 2.8.3)
project(robot_control)


find_package(catkin REQUIRED COMPONENTS
  eufs_description
  ackermann_msgs
  geometry_msgs
  gazebo_ros
  nav_msgs
  roscpp
  sensor_msgs
  std_msgs
  std_srvs
  tf
  diagnostic_msgs
  diagnostic_updater
)

catkin_package(
 CATKIN_DEPENDS ackermann_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(robot_control_node src/robot_control.cpp)

install(PROGRAMS
  nodes/ground_truth_republisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch/
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
   FILES_MATCHING PATTERN "*.launch" PATTERN "*.machine" PATTERN "*.yaml" PATTERN "*.urdf"
)

install(DIRECTORY config/
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
   FILES_MATCHING PATTERN "*.yaml"
)

target_link_libraries(robot_control_node
   ${catkin_LIBRARIES}
)

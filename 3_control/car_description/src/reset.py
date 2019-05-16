#!/usr/bin/env python
import rospy
import os

def reset():
	os.system('rostopic pub -1 /car/BackWheel_right_velocity_controller/command std_msgs/Float64 "data: 0"')
 
    	os.system('rostopic pub -1 /car/BackWheel_left_velocity_controller/command std_msgs/Float64 "data: 0"')

 	os.system('rostopic pub -1 /car/Turner_left_position_controller/command std_msgs/Float64 "data: 0"')

	os.system('rostopic pub -1 /car/Turner_right_position_controller/command std_msgs/Float64 "data: 0"')
 

if __name__ == '__main__':
    reset()




#!/usr/bin/env python
import rospy
import os
from geometry_msgs.msg import Twist


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x: %s y: %s", data.linear.x,data.angular.z)
    x=str(data.linear.x)
    os.system('rostopic pub -1 /car/BackWheel_right_velocity_controller/command std_msgs/Float64 "data: "'+x+'""')
    os.system('exit')
    os.system('rostopic pub -1 /car/BackWheel_left_velocity_controller/command std_msgs/Float64 "data: "'+x+'""')
    os.system('exit')
    if data.angular.z != 0:
    	y=data.angular.z*10
        if data.angular.z>0:
		y1=str(y)
		y2=str(y+10)
	os.system('rostopic pub -1 /car/Turner_left_position_controller/command std_msgs/Float64 "data: "'+y1+'""')
	os.system('exit')
	os.system('rostopic pub -1 /car/Turner_right_position_controller/command std_msgs/Float64 "data: "'+y2+'""')
	os.system('exit')    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/car/cmd_vel", Twist, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
	

if __name__ == '__main__':
    listener()




#!/usr/bin/env python
import rospy
import os
from geometry_msgs.msg import Twist
from std_msgs.msg      import Float64

rospy.init_node('controller', anonymous=True)
pubBR = rospy.Publisher('/car/BackWheel_right_velocity_controller/command', Float64, queue_size=10)
pubBL = rospy.Publisher('/car/BackWheel_left_velocity_controller/command', Float64, queue_size=10)
pubFR = rospy.Publisher('/car/Turner_right_position_controller/command', Float64, queue_size=10)
pubFL = rospy.Publisher('/car/Turner_left_position_controller/command', Float64, queue_size=10)

def callback(data):
    movementspeed = Float64()
    angleRight = Float64()
    angleLeft = Float64()
    rospy.loginfo(rospy.get_caller_id() + "I heard x: %s y: %s", data.linear.x,data.angular.z)
    movementspeed.data = data.linear.x
    pubBR.publish(movementspeed)
    pubBL.publish(movementspeed)
    if data.angular.z != 0:
    	y=data.angular.z 
	if data.angular.z > 0.2:
		y=0.2
        if data.angular.z>0:
		y1=y+0.05
		y2=y
	elif data.angular.z<0:
		y1=y
		y2=y+0.05
	else:
		y1=0.00001
		y2=0.00001
	angleRight.data = y1
        angleLeft.data = y2
	#Z IS REVERSED 
	pubFR.publish(angleLeft)
    	pubFL.publish(angleRight)


def move():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.Subscriber("/car/cmd_vel", Twist, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass








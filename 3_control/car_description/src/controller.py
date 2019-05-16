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
#test oti kanei publish  to minima se diaforetika topics 
#pubBR = rospy.Publisher('/BackRight', Float64, queue_size=10)
#pubBL = rospy.Publisher('/Backleft', Float64, queue_size=10)
#pubFR = rospy.Publisher('/frontr', Float64, queue_size=10)
#pubFL = rospy.Publisher('/frontl', Float64, queue_size=10)

def callback11(data):
    os.system('echo hi')
    rospy.loginfo(rospy.get_caller_id() + "I heard x: %s y: %s", data.linear.x,data.angular.z)
    x=str(data.linear.x)
    os.system('rostopic pub -1 /car/BackWheel_right_velocity_controller/command std_msgs/Float64 "data: "'+x+'""')
    os.system('exit')
    os.system('rostopic pub -1 /car/BackWheel_left_velocity_controller/command std_msgs/Float64 "data: "'+x+'""')
    os.system('exit')
    if data.angular.z != 0:
    	y=data.angular.z*10
        if data.angular.z>0:
		y1=str(y+0.1)
		y2=str(y)
	elif data.angular.z<0:
		y1=str(y)
		y2=str(y+0.1)
	else:
		y1=str(0)
		y2=str(0)
	os.system('rostopic pub -1 /car/Turner_left_position_controller/command std_msgs/Float64 "data: "'+y1+'""')
	os.system('rostopic pub -1 /car/Turner_right_position_controller/command std_msgs/Float64 "data: "'+y2+'""')
	os.system('exit')

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
        if data.angular.z>0:
		y1=y+0.1
		y2=y
	elif data.angular.z<0:
		y1=y
		y2=y+0.1
	else:
		y1=0
		y2=0
	angleRight.data = y1
        angleLeft.data = y2
	pubFR.publish(angleRight)
    	pubFL.publish(angleLeft)


def controller():

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
        controller()
    except rospy.ROSInterruptException: pass








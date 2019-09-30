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


def callback(data):
    #initialize variables
    movementspeed = Float64()
    angleRight = Float64()
    angleLeft = Float64()
    y_weight = 1
    #x_weight = 10
    y_max = 0.25
    #x_max = 100
    try:#check for weights and limits argotera na to kanw ana parametro to try
        x_weight = rospy.get_param('linear_weight_speed')
        x_max = rospy.get_param('linear_max_speed')
    except KeyError:
        print "values not set weight and limits will use default values"
    rospy.loginfo(rospy.get_caller_id() + "I heard x: %s y: %s", data.linear.x,data.angular.z)
    #forward movement
    movementspeed.data = data.linear.x #* x_weight
    #if movementspeed.data > x_max: #check if the linear forward speed extends forward speed limit
    #    movementspeed.data = x_max
    pubBR.publish(movementspeed)
    pubBL.publish(movementspeed)
    #Turning position
    y = data.angular.z * y_weight
    if y > 0.3 or y <-0.3: #check if the wheel position extends wheel position limit
        if y > 0:
            y=0.3
        if y < 0:
            y=-0.3
    if data.angular.z>0:
        y1=y+0.05
        y2=y
    elif data.angular.z<0:
        y1=y
        y2=y+0.05
    else:
        y1=0.00001
        y2=0.00001

    angleRight.data = y2
    angleLeft.data = y1
    pubFR.publish(angleRight)
    pubFL.publish(angleLeft)
    #change parameters for tf
    rospy.set_param('linear_wheel_speed',movementspeed.data)
    rospy.set_param('angular_wheel_position',y)

def move():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.Subscriber("/cmd_vel", Twist, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass








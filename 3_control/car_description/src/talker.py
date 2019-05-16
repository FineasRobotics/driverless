#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg      import Float64
import time


def talker():
    pub = rospy.Publisher('/car/cmd_vel', Twist, queue_size=10)
    #pub2 = rospy.Publisher('/car/BackWheel_right_velocity_controller/command', Float64, queue_size=10)
    #pub3 = rospy.Publisher('/car/BackWheel_left_velocity_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    vel_msg = Twist()
    #movementspeed = Float64()
    #movementspeed.data = 0.2
    # go forward then right	
    while not rospy.is_shutdown():
	#pub2.publish(movementspeed)
	#pub3.publish(movementspeed)
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = -0.2
	rospy.loginfo(vel_msg)
	pub.publish(vel_msg)
	time.sleep(10)
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	rospy.loginfo(vel_msg)
	pub.publish(vel_msg)
	time.sleep(10)
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0.2
        rospy.loginfo(vel_msg)
        pub.publish(vel_msg)
        rate.sleep()
	time.sleep(10)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

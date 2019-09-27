#!/usr/bin/env python
import sys
import os
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('tf_publisher')
odom_broadcaster = tf.TransformBroadcaster() # broadcasts tf msgs for base_footprint - odom


r = rospy.Rate(1.0)
while not rospy.is_shutdown():
   x = 1 
   y = 1
   x1 = 1
   y1 = 1
   w1 = 1
   pose = ""
   command = rosservice call gazebo/get_model_state "link_name: ''
   try:
   	pose = os.(command).read()
   except:
   	print "####ERROR#### couldnt use service" + pose
  	continue
   print pose
   # first, we'll publish the transform over tf
   odom_broadcaster.sendTransform(
        (x, y, 0.),
        (x1,y1,z1,w1),
        rospy.Time.now(),
        "base_footprint",
        "odom"
   )
   r.sleep()




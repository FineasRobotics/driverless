#!/usr/bin/env python
import rospy
from gazebo_msgs.srv import GetModelState
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3



rospy.init_node('tf_publisher') # initialize node
br = tf.TransformBroadcaster() # broadcasts tf msgs for base_footprint - odom
r = rospy.Rate(10.0)
# Band-aid untill the exception is fixxed.
r.sleep()
r.sleep()
r.sleep()
# 
br.sendTransform((0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "base_footprint",
                         "map")
while not rospy.is_shutdown():
   # first, we'll get the pose from gazebo api
   resp_coordinates = 0
   # !!Exception needs to be handled properly, nodes must be robust to different launching orders!!
   try:
	model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state',GetModelState)
	resp_coordinates = model_coordinates("car","")
	x = resp_coordinates.pose.position.x
   except rospy.ServiceException as e:
        rospy.loginfo("Get model State service call failed: {0}".format(e))
        break 
          #if rosservice fails abort - it can store last data and publish them instead of aborting ??
          #print "get some tf as proof of connectiong between map and robot " + str(x)
          # first, we'll publish the transform over tf
   br.sendTransform(
        (resp_coordinates.pose.position.x,resp_coordinates.pose.position.y,0),
        (resp_coordinates.pose.orientation.x ,resp_coordinates.pose.orientation.y ,resp_coordinates.pose.orientation.z ,resp_coordinates.pose.orientation.w),
        rospy.Time.now(),
        "base_footprint",
        "map"
   )
   r.sleep()


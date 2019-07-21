#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('dynamic_tf_listener')
  
    listener = tf.TransformListener() #store tf data
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(20.0)
    while not rospy.is_shutdown():
        try:
            rospy.loginfo(' new scan ')
            position,quaternion = listener.lookupTransform("base_footprint", "map", rospy.Time(0)) #look for tf between the world and the base 
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
		#re publish it
   	#br.sendTransform((position.[0], position.[1], 0),(quaternion.[0],quaternion.[1],quaternion.[2],quaternion.[3]),rospy.Time.now(),"base_footprint","map")
	print position,quaternion
        rate.sleep()

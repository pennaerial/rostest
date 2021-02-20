#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    try:
        publisher = rospy.Publisher('topic1', String, queue_size=10)
        rospy.init_node('publisher', anonymous=True)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            publisher.publish(hello_str)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

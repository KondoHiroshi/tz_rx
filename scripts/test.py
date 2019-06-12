#! /usr/bin/env python3

import sys
import time
import rospy
import threading
import std_msgs
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32


class test(object):
    def __init__(self):


        self.pub1 = rospy.Publisher("/test", Int32, queue_size=1)
        self.pub2 = rospy.Publisher("/test2", Int32, queue_size=1)
        self.sub1 = rospy.Subscriber("/test3", Int32, self.value)
        self.sub2 = rospy.Subscriber("/test4", Int32, self.value)

#switch
    def value(self,q):
        a = q.data
        self.pub2.publish(a)
        return



if __name__ == "__main__" :
    rospy.init_node("test")

    ctrl = test()

    rospy.spin()

#2018/11/01
#written by H.Kondo

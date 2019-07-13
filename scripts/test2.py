#! /usr/bin/env python3

import sys
import time
import rospy
import threading
import std_msgs
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32


class test2(object):
    def __init__(self):


        rospy.Subscriber("/test_latch_true", String, self.test1)
        rospy.Subscriber("/test_lacth_false", String, self.test2)

#switch
    def test1(self,q):
        print(q)
        return

    def test2(self,q):
        print(q)
        return


if __name__ == "__main__" :
    rospy.init_node("test2")

    ctrl = test2()

    rospy.spin()

#2018/11/01
#written by H.Kondo

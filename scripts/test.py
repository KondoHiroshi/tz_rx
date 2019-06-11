#! /usr/bin/env python3

import sys
import time

#sys.path.append("/home/amigos/ros/src/NASCORX_System-master")
import pymeasure

import rospy
import threading
import std_msgs
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32


class ml2437a_controller(object):
    def __init__(self):


        self.sub_power = rospy.Subscriber("/test", Int32, self.value)

#switch
    def value(self,q):
        a = q
        return a



if __name__ == "__main__" :
    rospy.init_node("test")

    ctrl = ml2437a_controller()

    rospy.spin()

#2018/11/01
#written by H.Kondo

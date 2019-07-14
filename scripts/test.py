#! /usr/bin/env python3

import sys
import time
import rospy
import threading
"""
import std_msgs
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32
"""

import std_msgs.msg

"""
class test(object):
    def __init__(self):

        self.pub1 = rospy.Publisher("/pub1", Int32, queue_size=1)
        self.pub2 = rospy.Publisher("/pub2", Int32, queue_size=1)
        self.pub3 = rospy.Publisher("/pub3", Int32, queue_size=1)
        self.pub4 = rospy.Publisher("/pub4", Int32, queue_size=1)
        self.pub5 = rospy.Publisher("/test", Int32, queue_size=1)
        self.sub1 = rospy.Subscriber("/sub1", Int32, self.test1)
        self.sub2 = rospy.Subscriber("/sub2", Int32, self.test2)
        self.sub3 = rospy.Subscriber("/sub3", Int32, self.test3)
        self.sub4 = rospy.Subscriber("/sub4", Int32, self.test4)


        self.latch_t = rospy.Publisher("/test_latch_true", String, queue_size=1,latch=True)
        self.latch_f = rospy.Publisher("/test_latch_false", String, queue_size=1,latch=False)

    def test1(self,q):
        a = q.data*1
        self.pub1.publish(a)
        return

    def test2(self,q):
        a = q.data*2
        self.pub2.publish(a)
        return

    def test3(self,q):
        a = q.data*3
        self.pub3.publish(a)
        return

    def test4(self,q):
        a = q.data*4
        self.pub4.publish(a)
        return

    def test_latch(self):
        t_list = ["1","2","3","4","5"]
        for i in t_list:
            time.sleep(0.1)
            self.latch_f.publish("latch false "+i)
            self.latch_t.publish("latch true "+i)
"""

class make_pub(object):

    def __init__(self):
        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
        time.sleep(0.01)
        return

class make_pub_test(object):

    def __init__(self):
        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = True)
        time.sleep(0.01)
        return

class test(object):

    def __init__(self):
        self.make_pub = make_pub_test()

    def test_f(self, data):
        topic_name = '/test_latch_false'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = data)
        return

    def test_t(self, data):
        topic_name = '/test_latch_false'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = data)
        return

if __name__ == "__main__" :
    rospy.init_node("test")

    ctrl = test()
    time.sleep(1)
    ctrl.test_f()

    rospy.spin()

#2018/11/01
#written by H.Kondo

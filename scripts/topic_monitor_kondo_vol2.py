#! /usr/bin/env python3

name = 'topic_monitor'

# ----
import time
import threading
import rospy
import std_msgs.msg


class topic_monitor(object):
    values = {}
    refreshing = False

    def __init__(self):

        self.values = {}
        self.refreshing = False
        self.topic_li = self.make_topic_list()
        self.make_sub()
        self.msgtype_dict = {
            'std_msgs/String': std_msgs.msg.String,
            'std_msgs/Float64': std_msgs.msg.Float64,
            'std_msgs/Int32': std_msgs.msg.Int32,
        }

    def make_topic_list(self):
        topic_li = []
        _topic_li = rospy.get_published_topics()
        for i in range(len(_topic_li)):
            if _topic_li[i][0] == '/rosout': pass
            elif _topic_li[i][0] == '/rosout_agg': pass
            else: topic_li.append(_topic_li[i])
        topic_li = sorted(topic_li)
        return topic_li

    def make_sub(self):
        topic_from = [rospy.Subscriber(
                    name = self.topic_li[i][0],
                    data_class = self.msgtype_dict[self.topic_li[i][1]],
                    callback = self.callback,
                    callback_args = {'name': self.topic_li[i][0]},
                    queue_size = 1,
                ) for i in range(len(self.topic_li))]

    def callback(self, msg, args):
        self.values[args['name']] = msg.data
        self.refresh()
        return

    def refresh(self):
        while self.refreshing == True:
            time.sleep(0.1)
            continue

        self.refreshing = True
        maxlen = max([len(_k) for _k in self.values.keys()])
        print('----')
        for key in sorted(self.values):
            print(('{0:<'+str(maxlen)+'} {1}').format(key, self.values[key]))
            continue
        self.refreshing = False

        now_topic_li = self.get_published_topics()
        now_topic_li = sorted(now_topic_li)
        if self._topic_li == now_topic_li:
            pass

        elif self._topic_li != now_topic_li:
            self._topic_li = now_topic_li
            self.make_sub()

        return


if __name__=='__main__':
    rospy.init_node(name)
    tm = topic_monitor()

    rospy.spin()

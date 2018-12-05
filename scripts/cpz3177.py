#! /usr/bin/env python3


import sys
import time
import numpy
import pyinterface

import rospy
from std_msgs.msg import Float64

sis_ch=8


if __name__ == '__main__':

    rospy.init_node('cpz3177')
    rate = rospy.get_param('~rate')
    rsw_id = rospy.get_param('~rsw_id')
    pm_ch = rospy.get_param("~pm_ch")
    node_name = 'cpz3177'

    ch_list = [("{0}".format(i)) for i in range(1, sis_ch + 1)]

    pub_list = [rospy.Publisher('{0}_rsw{1}_diff{2}'.format(node_name, rsw_id, ch), Float64, queue_size=1)
                       for ch in ch_list]

    pub_pm = rospy.Publisher('{0}_rsw{1}_diff{2}'.format(node_name, rsw_id, pm_ch),Float64, queue_size=1)

    try:
        ad = pyinterface.open(3177, rsw_id)
    except OSError as e:
        rospy.logerr("{e.strerror}. node={node_name}, rsw={rsw_id}".format(**locals()))
        sys.exit()

while not rospy.is_shutdown():

    msg = Float64()
    ret = ad.input_voltage(pm_ch, "diff")
    msg.data = ret
    pub_pm.publish(msg)

    for ch, pub in zip(ch_list, pub_list):
        ret = ad.input_voltage(ch, "diff")
        msg = Float64()
        msg.data = ret
        pub.publish(msg)
    time.sleep(rate)
    continue

#20181204
#change for Tz
#wriiten by Kondo

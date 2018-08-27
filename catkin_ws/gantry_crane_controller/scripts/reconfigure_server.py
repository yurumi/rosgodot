#!/usr/bin/env python2

import rospy

from dynamic_reconfigure.server import Server
from gantry_crane_controller.cfg import ControllerConfig

def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {u_max}, {controller_type}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("reconfigure_server", anonymous = False)

    srv = Server(ControllerConfig, callback)
    rospy.spin()

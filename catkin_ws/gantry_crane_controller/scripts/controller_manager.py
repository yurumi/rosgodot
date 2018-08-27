#!/usr/bin/env python2
import sys, os

import rospy
import dynamic_reconfigure.client
import controller_state_space

from geometry_msgs.msg import Wrench, Point
from gantry_crane_controller.msg import State


class GantryCraneControllerManager():
    def __init__(self):
        ## parameters
        self.rate = rospy.Rate(20)  # Hz
        self.u_max = 0.0    # maximaler Eingriff
        self.pos_cmd = 0.0  # Soll-Position
        self.controller_type = -1

        ## state vector
        self.state = State()

        ## controller
        self.controllers = {}
        self.controllers[1] = controller_state_space.ControllerStateSpace()

        ## Subscriber
        rospy.Subscriber('/gantry_crane/observed_state', State, self.StateCallback)
        rospy.Subscriber('/gantry_crane/pos_cmd', Point, self.PosCmdCallback)

        ## Publisher
        self.ctrl_msg = Wrench()
        self.pub = rospy.Publisher('/gantry_crane/body_force', Wrench, queue_size=10)

        ## Dynamic reconfigure
        rospy.loginfo('Waiting for reconfigure_server...')
        try:
            rospy.wait_for_service("reconfigure_server/set_parameters", timeout=30)
        except rospy.ROSException:
            rospy.logerr('...connection failed.')

        rospy.loginfo('...connected.')
        client = dynamic_reconfigure.client.Client("reconfigure_server", timeout=3, config_callback=self.ReconfigureCallback)

        ## Mainloop
        self.spin()


    def ReconfigureCallback(self, config):
        self.u_max = config['u_max']
        self.controller_type = config['controller_type']


    # Create a callback function for the subscriber.
    def StateCallback(self, data):
        self.state = data


    # Create a callback function for the subscriber.
    def PosCmdCallback(self, data):
        self.pos_cmd = data.x


    def spin(self):
        while not rospy.is_shutdown():
            ## Ausgabe
            if self.controller_type in self.controllers.keys():
                self.ctrl_msg.force.x = self.controllers[self.controller_type].update(self.state, self.pos_cmd, self.u_max)
            else:
                self.ctrl_msg.force.x = 0.0

            self.pub.publish(self.ctrl_msg)

            self.rate.sleep()


####################################################
####################################################
if __name__ == '__main__':
    rospy.init_node('controller_manager', anonymous=True)
    try:
        GantryCraneControllerManager()
    except rospy.ROSInterruptException:
        pass

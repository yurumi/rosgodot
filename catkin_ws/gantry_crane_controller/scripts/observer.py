#!/usr/bin/env python2
import rospy
import math
from gantry_crane_controller.msg import State
from geometry_msgs.msg import Pose

class GantryCraneObserver:

    def __init__(self):
        self.rate = rospy.Rate(100)
        self.outputState = State()

        rospy.Subscriber('/gantry_crane/measurements', Pose, self.PoseCallback)

        self.pub = rospy.Publisher('/gantry_crane/observed_state', State, queue_size=10)

        self.spin()


    # Create a callback function for the subscriber.
    def PoseCallback(self, data):
        self.outputState.x_crane = data.position.x
        self.outputState.vx_crane = data.orientation.x

        self.outputState.x_load = data.position.y
        self.outputState.vx_load = data.orientation.y

        self.outputState.phi_rod = data.orientation.w
        self.outputState.phi_rod_grad = self.outputState.phi_rod * 180 / 3.141

        print(self.outputState)

    def spin(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.outputState)

            self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node('gantry_crane_observer', anonymous = True)
    try:
        GantryCraneObserver()
    except rospy.ROSInterruptException:
        pass

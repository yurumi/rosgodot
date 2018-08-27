#!/usr/bin/env python2
import rospy

import numpy as np
import pickle
import sys, os

class ControllerStateSpace():
    def __init__(self):
        print('pwd: ', )
        data = pickle.load(open(os.path.dirname(os.path.abspath(__file__)) + '/params_acker.pkl', 'rb'))
        self.V = data['V']
        self.K = data['K']

        print('K_acker: ', np.array(self.K))
        print('V_acker: ', np.array(self.V))


    def update(self, state, pos_cmd, u_max):
        x = np.array([state.x_crane, state.vx_crane, state.phi_rod, state.dphi_rod])

        ## Regler
        return np.clip(-self.K.dot(x) + self.V * pos_cmd, -u_max, u_max)


####################################################
####################################################
if __name__ == '__main__':
    rospy.init_node('controller_ss', anonymous=False)
    try:
        ControllerStateSpace()
    except rospy.ROSInterruptException:
        pass

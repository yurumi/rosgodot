#!/usr/bin/env python2
import numpy as np
import pickle
import sys, os

from control import *

class Model():
    def __init__(self):
        ##############################
        ##### Zustandsraummodell
        ##############################
        l = 1.0 # Seillaenge
        m_k = 10.0 # Masse Laufkatze
        m_G = 10.0 # Masse Greifer
        g = 9.81 # Erdbeschleunigung

        a_23 = m_G * g / m_k
        a_43 = ((m_k + m_G) * g)/(m_k * l)
        b_2 = 1.0 / m_k
        b_4 = 1.0 / (m_k * l)

        ## Zustandsvektor x = [Position, Geschw., Winkel, Winkelgeschw.]
        self.A = np.array([[0., 1, 0, 0],
                           [0, 0, a_23, 0],
                           [0, 0, 0, 1],
                           [0, 0, -a_43, 0]])
        self.B = np.array([[0.], [b_2], [0], [-b_4]])
        self.C = np.array([[1., 0, 1, 0]])
        self.D = np.array([[0.]])
        self.sys = ss(self.A, self.B, self.C, self.D)

    def get_system_d(self, T):
        return self.sys.sample(T)


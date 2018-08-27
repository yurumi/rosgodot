#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pickle
import math

from control import *
from model import *


##############################
##### state space model
##############################
model = Model()

##############################
##### analysis
##############################
# T, yout = step_response(sys)
# T, yout = impulse_response(sys)

p = pole(model.sys)
print('poles (open loop): ', p)

##############################
##### synthesis
##############################
# pole placement (Ackermann)
# p_soll = [-5.1+0.0j, -4.2-0.0j, -5, -0.5] # kleine Winkel, kaum Ueberschwingen
p_soll = [-5.1+0.0j, -6.2-0.0j, -6, -1.0] #
K = acker(model.A, model.B, p_soll).getA()

# prefilter
V = np.linalg.inv([model.C.dot(np.linalg.inv(model.B.dot(K) - model.A)).dot(model.B)])

print('K: ', K)
print('V: ', V)

##############################
##### Plotting
##############################
# fig, ax = plt.subplots()
# ax.plot(T, yout)

# ax.set(xlabel='time (s)', ylabel='Step response')
# ax.grid()

# plt.show()


##############################
##### Save
##############################
with open('params_acker.pkl', 'wb') as f:
    data = {}
    data['poles_open_loop'] = p
    data['poles_closed_loop'] = p_soll
    data['K'] = K
    data['V'] = V
    pickle.dump(data, f, protocol=2)

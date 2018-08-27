#!/usr/bin/env python2

from __future__ import division

import os

from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt, Slot, qWarning
from python_qt_binding.QtWidgets import QWidget

import rospkg
import rospy
import rosservice
from geometry_msgs.msg import Point
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState

class GantryCraneWidget(QWidget):

    def __init__(self):
        super(GantryCraneWidget, self).__init__()
        self.setObjectName('GantryCraneWidget')

        # Create QWidget
        self._widget = QWidget()

        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_gantry_crane'), 'resource', 'GantryCrane.ui')

        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self)

        self.set_target_mark = rospy.ServiceProxy('gazebo/set_model_state', SetModelState)

        ## Signals & Slots
        self.ctrlButton_acker.clicked.connect(self.on_ctrlButton_acker_clicked)
        # self.ctrlButton_lqr.clicked.connect(self.on_ctrlButton_lqr_clicked)
        self.pos_cmd_slider.valueChanged.connect(self.on_pos_cmd_slider_changed)
        # self.pos_cmd_slider.sliderReleased.connect(self.on_pos_cmd_slider_released)
        self.posButton_L.clicked.connect(self.on_posButton_L_clicked)
        self.posButton_0.clicked.connect(self.on_posButton_0_clicked)
        self.posButton_R.clicked.connect(self.on_posButton_R_clicked)

        self.pos_cmd_pub = rospy.Publisher('/gantry_crane/pos_cmd', Point, queue_size=1)


    def get_cmd_pos(self):
        return self.pos_cmd_slider.value() / 100.0

    def set_target(self, x_cmd):
        ## Reactivate when Gazebo is available again.
        # req = ModelState(model_name='target')
        # req.pose.position.x = x_cmd
        # self.set_target_mark(req)

        pos = Point()
        pos.x = x_cmd
        self.pos_cmd_pub.publish(pos)

    @Slot()
    def on_ctrlButton_acker_clicked(self):
        pass
        # rospy.

    @Slot()
    def on_posButton_L_clicked(self):
        self.set_target(-3.0)

    @Slot()
    def on_posButton_0_clicked(self):
        self.set_target(0.0)

    @Slot()
    def on_posButton_R_clicked(self):
        self.set_target(3.0)


    @Slot(int)
    def on_pos_cmd_slider_changed(self):
        self.set_target(self.get_cmd_pos())


    # @Slot()
    # def on_pos_cmd_slider_released(self):
    #     pos = Point()
    #     pos.x = self.get_cmd_pos()
    #     self.pos_cmd_pub.publish(pos)
    #     print(pos)

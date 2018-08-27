#include "rosgodot.h"
#include <sstream>

#include <iostream>

RosGodot::RosGodot() {

  int argc = 0;

  // Announce this program to the ROS master as a "node" called "rosgodot"
  ros::init(argc, nullptr, "rosgodot");

  // Start the node resource managers (communication, time, etc)
  // ros::start();
  // Broadcast a simple log message
  // ROS_INFO_STREAM("Hello, world!");

  ros::NodeHandle n;
  m_publisher = n.advertise<geometry_msgs::Pose>("/gantry_crane/measurements", 1000);
  m_subscriber = n.subscribe("/gantry_crane/body_force", 1000, &RosGodot::controlMessageCallback, this);
  m_subscriber_pos_cmd = n.subscribe("/gantry_crane/pos_cmd", 1000, &RosGodot::posCmdMessageCallback, this);
}

RosGodot::~RosGodot() {
  ros::shutdown();
}

void RosGodot::spinOnce() {
  static int count(0);

  m_publisher.publish(m_measurements_msg);

  ros::spinOnce();

  count++;
}

void RosGodot::setMeasurementData(Vector3 pos_crane, double vel_crane,
                                  Vector3 pos_load, double vel_load,
                                  double rod_angle) {
  m_measurements_msg.position.x = pos_crane[0];
  m_measurements_msg.orientation.x = vel_crane;

  m_measurements_msg.position.y = pos_load[0];
  m_measurements_msg.orientation.y = vel_load;

  m_measurements_msg.orientation.w = rod_angle;
}

void RosGodot::_bind_methods() {

  ClassDB::bind_method(D_METHOD("spinOnce"), &RosGodot::spinOnce);
  ClassDB::bind_method(D_METHOD("setMeasurementData", "pos_crane", "vel_crane",
                                "pos_load", "vel_load",
                                "rod_angle"),
                       &RosGodot::setMeasurementData);

  ADD_SIGNAL(MethodInfo("control_msg_received", PropertyInfo(Variant::REAL, "control_input")));
  ADD_SIGNAL(MethodInfo("pos_cmd_msg_received", PropertyInfo(Variant::REAL, "pos_cmd")));
}

void RosGodot::controlMessageCallback(const geometry_msgs::Wrench::ConstPtr& msg) {
  // ROS_INFO("I heard: [%f]", msg->force.x);
  emit_signal("control_msg_received", msg->force.x);
}

void RosGodot::posCmdMessageCallback(const geometry_msgs::Point::ConstPtr& msg) {
  emit_signal("pos_cmd_msg_received", msg->x);
}

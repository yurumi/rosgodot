#ifndef ROSGODOT_H
#define ROSGODOT_H

#include "reference.h"
#include <ros/ros.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/Wrench.h>
#include <geometry_msgs/Point.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>

class RosGodot : public Reference {
  GDCLASS(RosGodot, Reference);

public:
  RosGodot();
  virtual ~RosGodot();

  void spinOnce();
  void setMeasurementData(Vector3 pos_crane, double vel_crane,
                          Vector3 pos_load, double vel_load,
                          double rod_angle);

protected:
  static void _bind_methods();
  void controlMessageCallback(const geometry_msgs::Wrench::ConstPtr& msg);
  void posCmdMessageCallback(const geometry_msgs::Point::ConstPtr& msg);

  ros::Publisher m_publisher;
  ros::Subscriber m_subscriber;
  ros::Subscriber m_subscriber_pos_cmd;
  geometry_msgs::Pose m_measurements_msg;
};

#endif

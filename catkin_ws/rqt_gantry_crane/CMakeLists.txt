cmake_minimum_required(VERSION 2.8.3)
project(rqt_gantry_crane)

find_package(catkin REQUIRED COMPONENTS
  rospy
  rqt_gui
  rqt_gui_py
)

catkin_package()
catkin_python_setup()

# include_directories(
# # include
#   ${catkin_INCLUDE_DIRS}
# )

install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/rqt_gantry_crane
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

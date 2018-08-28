# rosgodot

This repository is meant to be a proof of concept for interfacing the
open source game engine [Godot](https://godotengine.org) with the
[Robot Operating System](https://www.ros.org) (ROS).

## Introduction

## Installation (Linux)

### Godot
#### Compile the engine
 * Make sure the [requirements](http://docs.godotengine.org/en/3.0/development/compiling/compiling_for_x11.html) are met.
 * Get the sources:
 ```
 user@host:~$ git clone https://github.com/godotengine/godot.git
 ```
 * ```cd``` into cloned repository and compile with
 ```
 user@host:~/godot$ scons platform=x11
 ```
 * Normally, compiling is quite straight forward. If successfull, you can start the editor with ```./bin/godot.x11.tools.64``.
 * Close the editor.

#### Compile the rosgodot module
 * Clone this repository and copy ```<repo_clone_path>/rosgodot/godot/modules/rosgodot``` into the ```modules``` path in the godot sources (e.g. ```~/godot/modules``` for the above example).
 * Rebuild the engine:
 ```
 user@host:~/godot$ scons platform=x11
 ```
 * If successfull, the new Class ```RosGodot``` is available in GDScript.

#### Demo project
 * Start ```roscore```
 * Start the editor again (now with the rosgodot module build in).
 * In the project manager choose ```Import``` and navigate to the project file (```<repo_clone_path>/rosgodot/godot/gantry_crane_ros/project.godot```).
 * Press F5 (or the play button at the top right) to start the demo.
 * Nothing much will happen since the other ROS nodes are missing. ```rostopic list``` should show some new topics (```/gantry_crane/*```)

### ROS

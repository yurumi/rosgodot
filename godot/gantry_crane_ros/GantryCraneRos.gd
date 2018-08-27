extends Spatial

onready var CraneBody = get_node('Crane/Body')
onready var CraneLoad = get_node('Crane/Load')
onready var CraneCtrlVisualization = get_node('Crane/CtrlVisualization')
onready var TargetPosSprite = get_node('TargetPosSprite')
onready var Camera = get_node('Camera')

var rosnode
var ctrl_input = 0.0

# Called when the node enters the scene tree for the first time.
func _ready():
	rosnode = RosGodot.new()

	# Signals & Slots
	rosnode.connect('control_msg_received', self, 'on_control_msg_received')
	rosnode.connect('pos_cmd_msg_received', self, 'on_pos_cmd_msg_received')

func _physics_process(delta):
	var crane_pos = CraneBody.get_translation()
	var crane_vel_x = CraneBody.get_linear_velocity().x
	var load_pos = CraneLoad.get_translation()
	var load_vel_x = CraneLoad.get_linear_velocity().x
	var load_rot_z = CraneLoad.get_rotation().z

	rosnode.setMeasurementData(crane_pos, crane_vel_x, \
							   load_pos, load_vel_x, \
							   load_rot_z)

	rosnode.spinOnce()
	CraneBody.add_force(Vector3(ctrl_input / 2.5, 0, 0), Vector3(0, 0, 0))
	CraneCtrlVisualization.draw_ctrl_vis(crane_pos.x, ctrl_input)

	Camera.update_pose(crane_pos.x)


func on_control_msg_received(val):
	ctrl_input = val


func on_pos_cmd_msg_received(val):
	TargetPosSprite.translation.x = val

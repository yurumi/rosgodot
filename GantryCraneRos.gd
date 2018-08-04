extends Spatial

onready var CraneBody = get_node('Crane/Body')
onready var CraneLoad = get_node('Crane/Load')

var rosnode
var ctrl_input = 0.0

# Called when the node enters the scene tree for the first time.
func _ready():
	rosnode = Summator.new()

	# Signals & Slots
	rosnode.connect('control_msg_received', self, 'on_control_msg_received')

func _physics_process(delta):
	# print(CraneBody.get_translation())
	rosnode.setStateData(CraneBody.get_translation(), CraneBody.get_linear_velocity().x, \
						 CraneLoad.get_translation(), CraneLoad.get_linear_velocity().x, \
						 CraneLoad.get_rotation().z)
	rosnode.spinOnce()
	CraneBody.add_force(Vector3(ctrl_input/100.0, 0, 0), Vector3(0, 0, 0))

func on_control_msg_received(val):
	ctrl_input = val

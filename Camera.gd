extends Camera


const R = 3.1
var Dz_scale = 1.0
var Dz_const
var Dy_init

# Called when the node enters the scene tree for the first time.
func _ready():
	Dz_const = get_translation().z
	Dy_init = get_translation().y


func update_pose(target_pos_x):
	var Dz_circle = sqrt(pow(R, 2.0) - pow(target_pos_x, 2.0))
	var Dz = Dz_const + Dz_scale * Dz_circle
	set_translation(Vector3(target_pos_x, Dy_init, Dz))
	set_rotation(Vector3(0.0, target_pos_x * 0.1, 0.0))

extends Sprite3D

onready var Tween = get_node('Tween')

func _ready():
	Tween.interpolate_property(self, 'rotation_degrees', \
							   Vector3(90,0,0), Vector3(90, 360, 0), \
							   10.0, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	Tween.start()

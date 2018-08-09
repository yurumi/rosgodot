extends ImmediateGeometry


const u_scale = 0.01

func _ready():
	pass

func start():
	self.begin(Mesh.PRIMITIVE_TRIANGLES)

func commit():
	self.end()

func add_quad(verts, normal = Vector3(0, 0, 1)):
	self.set_normal(normal)
	self.add_vertex(verts[0])
	self.add_vertex(verts[1])
	self.add_vertex(verts[2])
	self.add_vertex(verts[2])
	self.add_vertex(verts[3])
	self.add_vertex(verts[0])

func draw_ctrl_vis(crane_pos_x, u):
	clear()
	self.start()

	var verts = []

	if u > 0.0:
		verts.append(Vector3(crane_pos_x, 0.8, 0))
		verts.append(Vector3(crane_pos_x, 1, 0))
		verts.append(Vector3(crane_pos_x + u * u_scale, 1, 0))
		verts.append(Vector3(crane_pos_x + u * u_scale, 0.8, 0))
	else:
		verts.append(Vector3(crane_pos_x, 0.8, 0))
		verts.append(Vector3(crane_pos_x + u * u_scale, 0.8, 0))
		verts.append(Vector3(crane_pos_x + u * u_scale, 1, 0))
		verts.append(Vector3(crane_pos_x, 1, 0))

	self.add_quad(verts)

	self.commit()

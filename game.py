import meet
import random

cells=[]
for i in range(20):
	cell1={"x":100, "y":200, "radius":random.randint(10,70), "dy":random.randint(-3,3),"dx":random.randint(-3,3), "color":"green"}
	z=meet.create_cell(cell1)
	cells.append(z)


user_cell={"x":99, "y":120, "radius":50, "dy":31,"dx":23, "color":"black"}
z=meet.create_cell(user_cell)
cells.append(z)

def borders(cells):
	for a in cells:
		w=get_screen_width()
		h=get_screen_height()
		


		if a.xcor()>=w:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.xcor()>=-w:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.ycor()>=h:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.ycor()>=-h:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
			





while True:
	dx,dy = meet.get_user_direction(z)
	z.set_dy(dy)
	z.set_dx(dx)
	meet.move_cells(cells)
	borders(cells)

	

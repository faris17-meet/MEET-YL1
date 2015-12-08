from meet import *
DOWN_EDGE

cells=[]
for x in range(13):
	get_random_x()
	get_random_y()
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":20, "dy":3,"dx":3, "color":"green"}
	z=create_cell(cell1)
	cells.append(z)
	for cell in cells
		if cell.xcor()>get_screen_width():
			cell.dx(-3)
 		if cell.xcor()>get_screen_width(*-1):
			cell.dx(-3)
		if cell.xcor()>get_screen_height()*-1:
			cell.dy(3)
		if cell.xcor()>get_screen_height()*-1:
			cell.dy(3)
while True:
        move_cells(cells)



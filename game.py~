#import meet
#import random

#cells=[]
#for i in range(20):
	#cell1={"x":100, "y":200, "radius":random.randint(10,70), "dy":random.randint(-3,3),"dx":random.randint(-3,3), "color":"green"}
	#z=meet.create_cell(cell1)
	#cells.append(z)


#user_cell={"x":99, "y":120, "radius":50, "dy":31,"dx":23, "color":"black"}
#z=meet.create_cell(user_cell)
#cells.append(z)

#def borders(cells):
	#for a in cells:
		#w=get_screen_width()
		#h=get_screen_height()
		


		#if a.xcor()>=w:
			#x=a.get_dx()
			#y=a.get_dy()
			#a.set_dx(-x)
			#a.set_dy(-y)
		#if a.xcor()>=-w:
			#x=a.get_dx()
			#y=a.get_dy()
			#a.set_dx(-x)
			#a.set_dy(-y)
		#if a.ycor()>=h:
			#x=a.get_dx()
			#y=a.get_dy()
			#a.set_dx(-x)
			#a.set_dy(-y)
		#if a.ycor()>=-h:
			#x=a.get_dx()
			#y=a.get_dy()
			#a.set_dx(-x)
			#a.set_dy(-y)
			





#while True:
	#dx,dy = meet.get_user_direction(z)
	#z.set_dy(dy)
	#z.set_dx(dx)
	#meet.move_cells(cells)
	#borders(cells)



import meet
import turtle
import random 
num_cells=0
colors=["purple",'blue','green','pink']
cells=[]
balls1={'radius':10,'x':88,'y':3 , 'dx' : 0 , 'dy' : 0, 'color':'yellow'}
circle1 = meet.create_cell(balls1)
cells.append(circle1)

while num_cells<15:
	balls={'radius':random.randint(1,17) ,'x':random.randint(-200,100),'y':random.randint(-200,100) ,'dx':random.randint(-1,1),'dy':random.randint(-1,1),'color':random.choice(colors)}

	num_cells+=1
	circle = meet.create_cell(balls)
	cells.append(circle)


def borders(cells):
	for cell in cells:		
		sw=meet.get_screen_width()
		sh=meet.get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x > sw):	
			cell.set_dx(-cell.get_dx())
		if (y > sh):
			cell.set_dy(-cell.get_dy())
		if (x < -sw):	
			cell.set_dx(-cell.get_dx())
		if (y < -sh):
			cell.set_dy(-cell.get_dy())
			

while True:
	x,y = meet.get_user_direction(circle1)
	
	circle1.set_dx(x)
	circle1.set_dy(y)
	borders(cells)	
	meet.move_cells(cells)
	for cell2 in cells:
		if(cell2 != circle1):
			a=circle1.xcor()
			b=circle1.ycor()
			r=circle1.radius
			c=cell2.xcor()
			d=cell2.ycor()
			r2=cell2.get_radius()
			if((a-c)**2 + (b-d)**2)**0.5 <= (r+r2):
				if(r>r2):
					cell2.goto(meet.get_random_x(),meet.get_random_y())
					circle1.set_radius(r+(r2/10))

				else:
				turtle.write("game over",align='center',font=('ariel', 30,'bold'))
				circle1.bye()

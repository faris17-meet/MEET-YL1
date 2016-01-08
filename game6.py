
import meet
import turtle
import random
import time

turtle.register_shape("skull.gif")
turtle.ht()
skull=turtle.clone()
skull.shape("skull.gif")
turtle.hideturtle()

skull.penup()
skull.goto(random.randint(-250,250),random.randint(-250,250))
skull.st()
skull.ondrag(skull.goto)



x=3
while x>0:
    turtle.hideturtle()
    turtle.color("black")
    turtle.write(" "+str(x),align='center',font=('ariel',80,'bold'))
    turtle.speed("slowest")
    time.sleep(0.4)
    turtle.clear()
    x-=1





colors=["purple",'blue','green','pink','red','brown','grey','maroon']
cells=[]
balls1={'radius':11,'x':0,'y':0 , 'dx' : 0 , 'dy' : 0, 'color':'yellow'}
myCircle = meet.create_cell(balls1)
cells.append(myCircle)

#black circle
balls2={'radius':30,'x':random.randint(-275,275),'y':random.randint(-275,275),'dx':random.randint(-1,3),'dy':random.randint(-1,1),'color':'black'}
badCircle = meet.create_cell(balls2)
cells.append(badCircle)

num_cells=0
while num_cells<12:
        balls={'radius':random.randint(3,25) ,'x':random.randint(-280,280),'y':random.randint(-280,280) ,'dx':random.randint(-1,1),'dy':random.randint(-1,1),'color':random.choice(colors)}
        num_cells+=1
        circle = meet.create_cell(balls)
        cells.append(circle)


def borders(cells):        
        for cell in cells:
            if(not cell == myCircle):
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
                        
        

score=0
game=True
while game:
        x,y = meet.get_user_direction(myCircle)
	
        myCircle.set_dx(x)
        myCircle.set_dy(y)
        borders(cells)	
        meet.move_cells(cells)
        for cell2 in cells:
                if(cell2 != myCircle):
                        myX=myCircle.xcor()
                        myY=myCircle.ycor()
                        myR=myCircle.radius
                        x=cell2.xcor()
                        y=cell2.ycor()
                        r=cell2.get_radius()
                        dist = ((myX - x)**2 + (myY - y)**2)**0.5
                        if dist <= (myR+r):
                            if (cell2 == badCircle):
                                score -=2
                                turtle.clear()
                                turtle.color("black")
                                turtle.penup()
                                turtle.goto(-270.0,250.0)
                                turtle.write("score:"+ str(score), align='center',font=('ariel',25,'bold'))
                                turtle.hideturtle()
                                badCircle.goto(meet.get_random_x(),meet.get_random_y())

                            elif (myR > r):
                                 cell2.goto(meet.get_random_x(),meet.get_random_y())
                                 myCircle.set_radius(myR+(r/39))
                                 if (cell2 != badCircle):
                                     score+=1
                                     turtle.clear()
                                     turtle.color("black")
                                     turtle.penup()
                                     turtle.goto(-270.0,250.0)
                                     turtle.write("score:"+ str(score), align='center',font=('ariel',25,'bold'))
                                     turtle.hideturtle()

                            else:
                                  turtle.color("red")                                       
                                  turtle.goto(-20.0,0)
                                  turtle.write("GAME OVER",align='center',font=('ariel',65,'bold'))
                                    
                                  circle.bye()
                                  game=False
                                  exit()
                                  break
                                        
                                        

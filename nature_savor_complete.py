import turtle
import time
turtle.setup(1000,650)
turtle.penup()
turtle.speed(0)
turtle.register_shape("bottle.gif")
turtle.register_shape("background.gif")
background=turtle.clone()
background.shape("background.gif")
turtle.register_shape("plastic_bag.gif")
turtle.register_shape("paper.gif")
turtle.register_shape("trash_can_paper.gif")
turtle.register_shape("trash_can_plastic.gif")
turtle.register_shape("trash_can_nylon.gif")
background.stamp()
turtle.ht()

trash_can_paper=turtle.clone()
trash_can_paper.shape("trash_can_paper.gif")
trash_can_plastic=turtle.clone()
trash_can_plastic.shape("trash_can_plastic.gif")
trash_can_nylon=turtle.clone()
trash_can_nylon.shape("trash_can_nylon.gif")
plastic_bottle_1=turtle.clone()
plastic_bottle_2=turtle.clone()
plastic_bottle_3=turtle.clone()
plastic_bottle_4=turtle.clone()
turtle.hideturtle()
plastic_bottle_1.ht()
plastic_bottle_1.shape("bottle.gif")
plastic_bottle_2.ht()
plastic_bottle_2.shape("bottle.gif")
plastic_bottle_3.ht()
plastic_bottle_3.shape("bottle.gif")
plastic_bottle_4.ht()
plastic_bottle_4.shape("bottle.gif")
plastic_bag_1=turtle.clone()
plastic_bag_1.shape("plastic_bag.gif")
plastic_bag_2=turtle.clone()
plastic_bag_2.shape("plastic_bag.gif")
plastic_bag_3=turtle.clone()
plastic_bag_3.shape("plastic_bag.gif")
plastic_bag_4=turtle.clone()
plastic_bag_4.shape("plastic_bag.gif")
paper_1=turtle.clone()
paper_1.shape("paper.gif")
paper_2=turtle.clone()
paper_2.shape("paper.gif")
paper_3=turtle.clone()
paper_3.shape("paper.gif")
paper_4=turtle.clone()
paper_4.shape("paper.gif")



print(type(paper_3))
    
#positions

plastic_bottle_1.penup()
plastic_bottle_1.goto(308,-201)
turtle.hideturtle()
plastic_bottle_1.st()
plastic_bottle_1.ondrag(plastic_bottle_1.goto)



plastic_bottle_2.penup()
plastic_bottle_2.goto(-101.0 , -225.0)
plastic_bottle_2.st()
plastic_bottle_2.ondrag(plastic_bottle_2.goto)


plastic_bottle_3.penup()
plastic_bottle_3.goto(-186,-97)
plastic_bottle_3.st()
plastic_bottle_3.ondrag(plastic_bottle_3.goto)


plastic_bottle_4.penup()
plastic_bottle_4.goto(-200,97)
plastic_bottle_4.st()
plastic_bottle_4.ondrag(plastic_bottle_4.goto)



plastic_bag_1.penup()
plastic_bag_1.goto(250 , 102)
plastic_bag_1.st()
plastic_bag_1.ondrag(plastic_bag_1.goto)



plastic_bag_2.penup()
plastic_bag_2.goto(-356,-107)
plastic_bag_2.st()
plastic_bag_2.ondrag(plastic_bag_2.goto)

plastic_bag_3.penup()
plastic_bag_3.goto(-204,52)
plastic_bag_3.st()
plastic_bag_3.ondrag(plastic_bag_3.goto)


plastic_bag_4.penup()
plastic_bag_4.goto(120 , 165)
plastic_bag_4.st()
plastic_bag_4.ondrag(plastic_bag_4.goto)


paper_1.penup()
paper_1.goto(10,-125)
paper_1.st()
paper_1.ondrag(paper_1.goto)

paper_2.penup()
paper_2.goto(50,-232)
paper_2.st()
paper_2.ondrag(paper_2.goto)


paper_3.penup()
paper_3.goto(413.0 , -172.0)
paper_3.st()
paper_3.ondrag(paper_3.goto)


paper_4.penup()
paper_4.goto(73,-225)
paper_4.st()
paper_4.ondrag(paper_4.goto)

trash_can_paper.goto(380,220)
trash_can_paper.st()
trash_can_plastic.goto(-278,220)
trash_can_plastic.st()
trash_can_nylon.goto(10,220)
trash_can_nylon.st()


def printloc(x,y):
    print (x,y)

turtle.onscreenclick(printloc)

#timer
timer=turtle.clone()
timer.penup()
timer.goto(-337,-234)
timer.color('blue')
clock=23
def countdown():
    font=24
    global clock
    timer.clear()
    timer.write(str(clock),font=('ariel',font,'bold'))
    clock-=1
    turtle.ontimer(countdown,1000)
    if clock==5:
        global font
        font=40
        timer.pencolor('red')
        #timer.write(time,font=('ariel',font,'bold')
    elif clock==-1:
        timer.clear()
        timer.write('GAME OVER',font=('ariel',70,'bold'))
        time.sleep(1)
        turtle.bye()
        exit()
        turtle.outimer(countdown)

        
countdown()

#move,check


bottle_list=[plastic_bottle_1,plastic_bottle_2,plastic_bottle_3,plastic_bottle_4]
plastic_bag_list=[plastic_bag_1,plastic_bag_2,plastic_bag_3,plastic_bag_4]
paper_list=[paper_1,paper_2,paper_3,paper_4]
bottle_loc=[(308,-201),(-101.0 , -225.0),(-186,-97),(-200,97)]
plastic_bag_loc=[(250 , 102),(-356,-107),(-204,52),(120 , 165)]
paper_loc=[(10,-125),(50,-232),(413.0 , -172.0),(73,-225)]
score=0 #copy
score_turtle=turtle.clone()
score_turtle.goto(400.0 ,300.0)


def check():
    global score
 #   print("check function called")
    for i in bottle_list:
        print("bottle distance ", i.distance(trash_can_plastic))
        if i.distance(trash_can_plastic)<=100:
            i.ht()
            bottle_list.remove(i)
            score+=1

    for i in plastic_bag_list: 
        if i.distance(trash_can_nylon)<=100:
            i.ht()
            plastic_bag_list.remove(i)
            score+=1

                        
    for i in paper_list:
        if i.distance(trash_can_paper)<=100:
            i.ht()
            paper_list.remove(i)
            score+=1
    score_turtle.clear()
    font=14
    score_turtle.write("score: "+ str(score), font=('ariel', font, 'bold') )       


        #goodjob

    if bottle_list==[] and plastic_bag_list==[] and paper_list==[]:
        timer.clear()
        timer.write('Good Job!',font=('arial',70,'bold'))
        time.sleep(2)
        turtle.bye()
        exit()

    turtle.ontimer(check, 100)
check()


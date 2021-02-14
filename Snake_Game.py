#Simple SnakeGame in python:
import turtle
import time
import random

delay=0.1
#Score
score=0
high_score=0

#Set up the screen
win=turtle.Screen()
win.title("Snake Game By Upasana Majhi")
win.bgcolor("green")
win.setup(width=600,height=600)
win.tracer(0)#turns off the screen updates
#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()#So that does not draw anything
head.goto(0,0)#From centre of the screen
head.direction="stop"

#Snake food code
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()#So that does not draw anything
food.goto(0,100)#From centre of the screen
segments=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0",align="center",font=("Courier",24,'normal'))


#Function for the movement of the snake
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)#we can also do like head.setx(head.xcor()+20)
#keyboard binding
#Connect a key press with a particular function
win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")


#Main game loop
while True:
    win.update()
    #Check for a collision with thw boarder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        
    #Check for collision with the food
    if head.distance(food) <20:
        # Move the food to a random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    #Add a segment
        new_segment=turtle.Turtle()  #object create
        new_segment.speed(0)#Animation speed not speed of movement
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    #shorten the delay
    

    #Increase the score:
        score +=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,'normal'))
#Move the end segemnt 1st in reverse order
    for index in range(len(segments)-1,0,-1):#range[start:end:step]
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0 to where the head is
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()#call the func here
    #Check  for head collision with the segments
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            #Clear the segments list
            segments.clear()
            #Reset the score
            score=0
            pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,'normal'))
    time.sleep(delay)

win.mainloop()
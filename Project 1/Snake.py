#This is a simple snake game made using Python 3
#By Aaron Avers
#Inspired by @TokyoEdTech's Python Game Programming Tutorial: Snake Game

import time
import turtle
import random

delay = 0.2

#Score
score = 0
high_score = 0

#Create screen 
screen = turtle.Screen()
screen.title("Snake Game by UnderratedRon")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#Keybinds
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")


#Game Loop
while True:
    screen.update()

    #check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()
        
        #Reset the score
        score = 0

        #Reset the delay
        delay = 0.2

        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment to the snakes body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.002

        #Increase the score
        score += 100

        if score > high_score:
            high_score =score
        
        pen.clear()
        pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))


    #Moving the segments starting at the end
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        

    move()

    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

            #Reset the score
            score = 0

            #Reset the delay
            delay = 0.2

            pen.clear()
            pen.write("Score: {} High Score: {}". format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)





screen.mainloop()
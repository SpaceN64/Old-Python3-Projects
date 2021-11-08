import turtle
import os
import math
import random
from random import randint

# Set Up Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Get to the End!")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.hideturtle()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

# Draw Winning Area
win_pen = turtle.Turtle()
win_pen.shape("square")
win_pen.penup()
win_pen.setposition(0,267.7)
win_pen.shapesize(3,29.8)


score = 0

# Show Score on Screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 303)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Ubuntu", 14, "normal"))
score_pen.hideturtle()

# Set up Player 1
player1 = turtle.Turtle()
player1.color("blue")
player1.shape("triangle")
player1.penup()
player1.speed(0)
player1.setposition(0, -250)
player1.setheading(90)
player1speed = 15

# Set Up Enemies
en = 8
enemies = []
for i in range(en):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("square")
    enemy.penup()
    enemy.speed(0)
    enemy.goto(randint(-280,280),randint(-280,280))
    enemy.shapesize(2,2)
    enemyspeed = 2

# Draw Winning Area
win_pen = turtle.Turtle()
win_pen.hideturtle()
win_pen.shape("square")
win_pen.penup()
win_pen.setposition(0,267.7)
win_pen.shapesize(3,29.8)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

def left():
    x = player1.xcor()
    player1.setheading(180)
    player1.forward(player1speed)
    if x < -280:
        x = - 280
        player1.setx(x)

def right():
    x = player1.xcor()
    player1.setheading(0)
    player1.forward(player1speed)
    if x > 280:
        x = 280
        player1.setx(x)

def up():
    y = player1.ycor()
    player1.setheading(90)
    player1.forward(player1speed)
    if y > 280:
        y = -250
        player1.sety(y)


def down():
    y = player1.ycor()
    player1.setheading(270)
    player1.forward(player1speed)
    if y < -280:
        y = 280
        player1.sety(y)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(up, "w")
turtle.onkey(down, "s")


# Main Loop
while True:
    wn.update()
    # Winning
    y = player1.ycor()
    if y > 280:
        y = -250
        player1.sety(y)
        # Update Score
        score += 1
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Ubuntu", 14, "normal"))
        for i in range(en):
            enemies.append(turtle.Turtle())
        for enemy in enemies:
            enemy.goto(randint(-280,280),randint(-280,280))

    if isCollision(player1, enemies):
        player1.hideturtle()
        for enemy in enemies:
            enemy.hideturtle()
        print ("Game Over")
        break


        
wn.mainloop()

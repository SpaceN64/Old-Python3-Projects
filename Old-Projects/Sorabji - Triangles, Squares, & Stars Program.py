import turtle as t

t.bgcolor("black")
t.speed("fast")

t.pencolor("blue")

t.penup()
t.goto(90,90)
t.pendown()

for i in range(40):
    t.forward(50)
    t.left(123)

    
t.pencolor("yellow")

t.penup()
t.goto(253,-284)
t.pendown()

for i in range(41):
    t.forward(100)
    t.left(123)


t.pencolor("red")

t.penup()
t.goto(-196,284)
t.pendown()

for i in range(74):
    t.forward(75)
    t.right(91.23)


t.pencolor("white")

t.penup()
t.goto(-90,-90)
t.pendown()

for i in range(82):
    t.forward(75)
    t.right(123)
    

t.pencolor("green")

t.penup()
t.goto(-100,-270)
t.pendown()

for i in range(20):
    t.forward(i * 10)
    t.right(144)

import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.goto(-200,0)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)
t.penup()
t.goto(-200,200)
t.pendown()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.penup()
t.goto(0,250)
t.pendown()
t.circle(50)



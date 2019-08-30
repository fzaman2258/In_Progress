import turtle
import tkinter

t=turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.penup()
t.forward(200)
t.pendown()
t.speed(10)   # cap speed
t.pencolor("purple")
t.pensize(50)
for i in range (0,50):
    t.forward(i)
    t.left(91)

t.pencolor("red")
for i in range(0,50):
    t.pensize(i)
    t.forward(10)




turtle.done()

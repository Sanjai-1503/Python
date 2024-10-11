import turtle
from turtle import Turtle,Screen
import random
t=Turtle()
t.shape()
t.speed(100)
t.penup()
x=-300
y=-300
t.setx(x)
t.sety(y)


turtle.colormode(255)
for i in range(1,200):
    t.dot(15,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t.forward(40)
    if i%15==0:
        y+=40
        x=-300
        t.sety(y)
        t.setx(x)








screen=Screen()
screen.exitonclick()

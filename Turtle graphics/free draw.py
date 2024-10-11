from turtle import Turtle,Screen
t=Turtle()
t.pensize(20)
t.pencolor("red")
def pen():
    t.penup()
def pen2():
    t.pendown()
def up():
    t.forward(10)
def down():
    t.backward(10)

def rangle():
    t.right(10)

def langle():
    t.left(10)






screen=Screen()
screen.listen()
screen.onkey(key="w",fun=up)
screen.onkey(key="s",fun=down)
screen.onkey(key="k",fun=rangle)
screen.onkey(key="l",fun=langle)
screen.onkey(key="p",fun=pen)
screen.onkey(key="o",fun=pen2)
screen.exitonclick()
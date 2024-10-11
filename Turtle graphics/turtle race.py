from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)

players=["red","blue","orange",'brown',"green"]
pos=-100

user_color=screen.textinput("Race","Bet your colour:")
all_turtle=[]
f=False


for color in players:
    San=Turtle()
    San.penup()
    San.shape("turtle")
    San.color(color)
    San.goto(-230,pos)
    pos+=50
    all_turtle.append(San)
if user_color:
    f=True
while f:
    for i in all_turtle:
        i.forward(random.randint(1,10))
        if i.xcor()>230:
            winning_color=i.pencolor()
            if user_color==winning_color:
                print("You Win")
            else:
                print(f"You Lose ,Winning color is {winning_color}")
            f=False



screen.exitonclick()

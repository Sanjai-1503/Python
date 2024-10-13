import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.random()

    def random(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

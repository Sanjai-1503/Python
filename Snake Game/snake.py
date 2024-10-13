import random
from turtle import Turtle

up = 90
down = 270
right = 0
left = 180


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.colours = ["black","white"]

    def initial_snake(self):
        x = 0
        for i in range(3):
            snake = Turtle(shape="square")

            snake.penup()
            snake.color(random.choice(self.colours))
            snake.setx(x)
            x -= 20
            self.all_snakes.append(snake)

    def new_one(self):
        new = Turtle("square")
        new.penup()
        new.goto(self.all_snakes[-1].position())
        new.color(random.choice(self.colours))
        self.all_snakes.append(new)

    def move(self):

        for i in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[i - 1].xcor()
            new_y = self.all_snakes[i - 1].ycor()
            self.all_snakes[i].goto(new_x, new_y)
        self.all_snakes[0].forward(20)

    def up(self):
        if self.all_snakes[0].heading() != down:
            self.all_snakes[0].setheading(90)

    def down(self):
        if self.all_snakes[0].heading() != up:
            self.all_snakes[0].setheading(270)

    def right(self):
        if self.all_snakes[0].heading() != left:
            self.all_snakes[0].setheading(0)

    def left(self):
        if self.all_snakes[0].heading() != right:
            self.all_snakes[0].setheading(180)

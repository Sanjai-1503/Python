from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x = 10
        self.y = 10
        self.speed = 0.1

    def move(self):
        x_c = self.xcor() + self.x
        y_c = self.ycor() + self.y
        self.goto(x_c, y_c)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()

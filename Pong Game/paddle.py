from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, l, wid):
        super().__init__()
        self.penup()
        self.shapesize(l, wid)
        self.shape("square")
        self.color("white")
        self.goto(pos)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

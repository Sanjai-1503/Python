from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))

    def l_update(self):
        self.l_score += 1
        self.clear()
        self.update()

    def r_update(self):
        self.r_score += 1
        self.clear()
        self.update()

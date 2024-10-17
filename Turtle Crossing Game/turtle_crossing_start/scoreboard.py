from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level:{self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

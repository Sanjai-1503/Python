from turtle import Turtle


class Score(Turtle):
    def __init__(self, val):
        super().__init__()
        self.hideturtle()
        self.val = val
        self.penup()
        self.goto(0, 265)
        self.write(f"Score :0", False, align="center", font=("Arial", 16, "bold"))

    def update(self):
        self.clear()
        self.val+=1
        self.write(f"Score :{self.val}", False, align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Veliya Podaa..", False, align="center", font=("Arial", 16, "bold"))

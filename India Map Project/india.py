import turtle
import pandas as pd


screen = turtle.Screen()
screen.setup(720, 750)
img = "india50.gif"
screen.addshape(img)
turtle.shape(img)
data = pd.read_csv("states_data.csv")
states = data["state"].to_list()
Guessed = []


def click(x, y):
    st = screen.textinput(title=f"{len(Guessed)}/29", prompt="Enter State").title()
    new = turtle.Turtle()
    new.penup()
    new.hideturtle()

    if st in states:
        if st in Guessed:
            screen.textinput(title="Already Guessed", prompt="Try Once")
        else:
            Guessed.append(st)
            new.goto(x, y)
            new.write(st, font=("arial", 10, "bold"))
    else:
        go = screen.textinput(title="You Guessed wrong", prompt="Game Over")
        if go == "exit":
            missing = []
            for i in states:
                if i not in Guessed:
                    missing.append(i)
            df = pd.DataFrame(missing)
            df.to_csv("States_to_learn.csv")
            screen.exitonclick()


turtle.onscreenclick(click)

turtle.mainloop()

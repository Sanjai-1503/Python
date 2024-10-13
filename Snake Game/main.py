import time
import turtle
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("sky blue")
screen.title("Snake Game")
turtle.colormode(255)
colours = ["red", "black", "yellow", "brown", "orange", "white"]
all_snakes = []
screen.tracer(0)
val = 0
snake = Snake()
food = Food()
score = Score(val)

snake.initial_snake()

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    snake.move()
    if snake.all_snakes[0].distance(food) < 15:
        food.random()
        snake.new_one()
        score.update()

    if snake.all_snakes[0].xcor() > 280 or snake.all_snakes[0].xcor() < -280 or snake.all_snakes[0].ycor() > 280 or \
            snake.all_snakes[0].ycor() < -280:
        score.game_over()
        game_on = False
    screen.update()
    time.sleep(0.1)

    for snake in all_snakes:
        if snake == all_snakes[0]:
            pass
        elif all_snakes[0].distance(snake) > 10:
            game_on = False
            score.game_over()

screen.exitonclick()

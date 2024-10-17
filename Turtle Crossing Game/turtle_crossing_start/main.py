import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if player.ycor() > 280:
        player.update_player()
        score.update_score()
        speed *= 0.8

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()

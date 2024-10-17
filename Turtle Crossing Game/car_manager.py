from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        rand = random.randint(1, 6)
        if rand == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(310, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for i in self.all_cars:
            i.backward(STARTING_MOVE_DISTANCE)

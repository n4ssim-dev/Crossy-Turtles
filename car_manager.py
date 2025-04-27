import random
import time
from turtle import Turtle

from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WAITING_TIME = 2

class CarManager(Scoreboard):
    def __init__(self):
        super().__init__()
        self.score = Scoreboard().score
        self.cars = []
        self.create_car()

    def create_car(self):
        random_color = random.choice(COLORS)
        random_number = random.randint(0,6)

        if random_number == 5:
            car = Turtle("square")
            car.setheading(180)
            car.shapesize(1, 2)
            car.penup()
            car.color(random_color)
            car.goto(330, random.randint(-220, 250))
            self.cars.append(car)

    def move_cars(self):
        forward_distance = STARTING_MOVE_DISTANCE + self.score * MOVE_INCREMENT
        for car in self.cars:
            car.forward(forward_distance)

    def clear_cars(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()
        self.cars.clear()

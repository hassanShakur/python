from turtle import Turtle
from random import randint, choice

COLORS = ["red", "blue", "violet", "yellow", "green"]
MOVE_DISTANCE = 10
MOVE_SPEED = 10


class CarGenerator:
    def __init__(self) -> None:
        self.cars = []
        self.speed = MOVE_SPEED
        self.high_chance = 5

    def create_car(self):
        gen_chance = randint(1, self.high_chance)
        if gen_chance != 1:
            return
        car = Turtle("square")
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(choice(COLORS))
        car.goto(x=400, y=randint(-250, 250))
        self.cars.append(car)

    def get_moving(self):
        for car in self.cars:
            car.forward(self.speed)

    def gen_more_cars(self):
        self.high_chance -= 1

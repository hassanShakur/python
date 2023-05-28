from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_food_props()
        self.re_position()

    def create_food_props(self):
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def re_position(self):
        x_pos = random.randint(-380, 380)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)

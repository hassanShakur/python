from turtle import Turtle
import random


class Food:
    def __init__(self) -> None:
        self.food = self.create_food_props()
        self.re_position()
        

    def create_food_props(self):
        food = Turtle('circle')
        food.color("green")
        food.penup()
        food.speed("fastest")
        food.shapesize(stretch_wid=0.5, stretch_len=0.5)
        return food
    
    def re_position(self):
        x_pos = random.randint(-380, 380)
        y_pos = random.randint(-280, 280)
        self.food.goto(x_pos, y_pos)
        

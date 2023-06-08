from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.y_angle_speed = 10
        self.x_angle_speed = 10

    def move(self):
        new_y = self.ycor() + self.y_angle_speed
        new_x = self.xcor() + self.x_angle_speed
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_angle_speed *= -1
from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_foward(self):
        if self.ycor() == 280:
            return
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() == -280:
            return
        self.backward(MOVE_DISTANCE)

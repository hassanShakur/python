from turtle import Turtle

MOVE_DISTANCE = 10
START_LINE = (0, -280)
START_POINT = -280
FINISH_POINT = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def goto_start(self):
        self.goto(START_LINE)

    def move_foward(self):
        if self.ycor() == FINISH_POINT:
            self.goto_start()
            return
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() == START_POINT:
            return
        self.backward(MOVE_DISTANCE)

from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.roll_speed = 0.1
        self.y_angle_speed = 10
        self.x_angle_speed = 10

    def move(self):
        new_y = self.ycor() + self.y_angle_speed
        new_x = self.xcor() + self.x_angle_speed
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_angle_speed *= -1

    def paddle_bounce(self):
        self.x_angle_speed *= -1
        # Increase speed by gradually reducing sleep time
        self.roll_speed *= 0.94

    def player_missed(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.roll_speed = 0.1

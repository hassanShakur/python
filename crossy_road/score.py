from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.color("white")
        self.goto(-350, 270)
        self.write_level()
        self.hideturtle()

    def write_level(self):
        self.clear()
        self.write(
            arg=f"Level: {self.level}", align="center", font=("Arial", 16, "normal")
        )

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over!", align="center", font=("Arial", 18, "normal"))

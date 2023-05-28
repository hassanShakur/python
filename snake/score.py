from turtle import Turtle


class Score(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}", align="center", font=("Arial", 16, "normal")
        )

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over!", align="center", font=("Arial", 18, "normal"))

from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-80, y=270)
        self.write(arg=self.left_score, align="center", font=("Arial", 20, "normal"))
        self.goto(x=80, y=270)
        self.write(arg=self.right_score, align="center", font=("Arial", 20, "normal"))

    def update_score(self, player):
        if player == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
        self.write_score()
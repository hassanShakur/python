from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in START_POS:
            self.extend(pos)

    def extend(self, position):
        tur = Turtle("square")
        tur.color("white")
        tur.penup()
        tur.goto(position)
        self.snake.append(tur)

    def grow(self):
        self.extend(self.snake[-1].position())

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            x_goto = self.snake[part - 1].xcor()
            y_goto = self.snake[part - 1].ycor()
            self.snake[part].goto(x_goto, y_goto)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

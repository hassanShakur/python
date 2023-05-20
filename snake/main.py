from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Slitherer")
screen.setup(width=800, height=600)
screen.tracer(0)


start_pos = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for pos in start_pos:
    tur = Turtle("square")
    tur.color("white")
    tur.penup()
    tur.goto(pos)
    snake.append(tur)


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    for part in range(len(snake) - 1, 0, -1):
        x_goto = snake[part - 1].xcor()
        y_goto = snake[part - 1].ycor()
        snake[part].goto(x_goto, y_goto)

    snake[0].forward(20)
    snake[0].left(90)


screen.exitonclick()

from turtle import Screen
import time
from slitherer import Snake
from food import Food


screen = Screen()
screen.bgcolor("black")
screen.title("Slitherer")
screen.setup(width=800, height=600)
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for colission
    if snake.head.distance(food.food) < 15:  # As food is 10x10
        food.re_position()


screen.exitonclick()

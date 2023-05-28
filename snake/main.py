from turtle import Screen
import time
from slitherer import Snake
from food import Food
from score import Score


screen = Screen()
screen.bgcolor("black")
screen.title("Slitherer")
screen.setup(width=800, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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

    # Check for colission with food
    if snake.head.distance(food) < 16:  # As food is 10x10
        food.re_position()
        score.update_score()
        snake.grow()

    # Check for colission with wall
    if (
        snake.head.xcor() < -380
        or snake.head.xcor() > 380
        or snake.head.ycor() < -280
        or snake.head.ycor() > 280
    ):
        game_on = False
        score.game_over()

    # Colission with self => Slice head
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            score.game_over()


screen.exitonclick()

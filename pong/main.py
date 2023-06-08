from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Hide animation for manual screen update
screen.tracer(0)

left_paddle = Paddle((360, 0))
right_paddle = Paddle((-370, 0))
ball = Ball()

# Listen to key strokes
screen.listen()

# Left paddle moves upon Up & Down
screen.onkeypress(left_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "Down")

# Right paddle moves upon A & Z
screen.onkeypress(right_paddle.move_up, "a")
screen.onkeypress(right_paddle.move_down, "z")

game_on = True

while game_on:
    # Sleep a while to slow movement
    time.sleep(0.1)
    # Update screen animations
    screen.update()
    ball.move()

    # Roof & Floor collision
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce()


screen.exitonclick()

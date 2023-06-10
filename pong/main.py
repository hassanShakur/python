from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Hide animation for manual screen update
screen.tracer(0)

right_paddle = Paddle((360, 0))
left_paddle = Paddle((-370, 0))
ball = Ball()
score = Score()

# Listen to key strokes
screen.listen()

# Left paddle moves upon Up & Down
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# Right paddle moves upon A & Z
screen.onkeypress(left_paddle.move_up, "a")
screen.onkeypress(left_paddle.move_down, "z")

game_on = True

while game_on:
    # Sleep a while to slow movement
    time.sleep(ball.roll_speed)
    # Update screen animations
    screen.update()
    ball.move()

    # Roof & Floor collision
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.wall_bounce()

    # Paddle collision
    if (
        ball.distance(right_paddle) < 60
        and ball.xcor() > 339
        or ball.distance(left_paddle) < 60
        and ball.xcor() < -349
    ):
        ball.paddle_bounce()

    # Player missed
    if ball.xcor() > 342:
        ball.player_missed()
        score.update_score("left")

    if ball.xcor() < -352:
        ball.player_missed()
        score.update_score("right")


screen.exitonclick()

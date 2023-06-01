from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Hide animation for manual screen update
screen.tracer(0)

left_paddle = Paddle((360, 0))
right_paddle = Paddle((-370, 0))

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
    # Update screen animations
    screen.update()


screen.exitonclick()
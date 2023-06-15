from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossy Road")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()

screen.onkeypress(player.move_foward, 'Up')
screen.onkeypress(player.move_backward, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()

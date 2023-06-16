from turtle import Screen
from player import Player
from score import Score
from car_generator import CarGenerator
import time

UP_SPEED = 2

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossy Road")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
score = Score()
car_gen = CarGenerator()

screen.onkeypress(player.move_foward, "Up")
screen.onkeypress(player.move_backward, "Down")

game_is_on = True

while game_is_on:
    car_gen.get_moving()
    car_gen.create_car()
    time.sleep(0.1)
    screen.update()

    # Colission with car
    for car in car_gen.cars:
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()

    # Increase speed on reaching finish line
    if player.ycor() == 280:
        player.goto_start()
        score.level_up()
        car_gen.speed += UP_SPEED

        if score.level % 5 == 0:
            car_gen.gen_more_cars()


screen.exitonclick()

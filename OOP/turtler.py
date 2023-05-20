# from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
lisa = t.Turtle()
scr = t.Screen()


# lisa.color("DeepPink")
lisa.shape("classic")
# lisa.pensize(2)
lisa.speed("fastest")

angles = [0, 90, 180, 270]


def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spiral(size):
    for _ in range(int(360 / size)):
        lisa.color(create_color())
        lisa.circle(100)
        lisa.setheading(lisa.heading() + size)
        lisa.penup()
        lisa.forward(3)
        lisa.pendown()


# draw_spiral(5)
scr.clear()
comment = scr.textinput(title="Write something", prompt="What do you wanna say")
print(comment)


def key_press_handler():
    lisa.forward(100)


scr.listen()
scr.onkey(key_press_handler, "space")
scr.exitonclick()

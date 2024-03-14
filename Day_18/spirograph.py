import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.speed('fastest')
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


angle = 0
while angle != 360:
    tim.setheading(angle)
    tim.color(random_color())
    tim.circle(100)
    angle += 5

screen = Screen()
screen.exitonclick()

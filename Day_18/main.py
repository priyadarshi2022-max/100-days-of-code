import colorgram
import turtle as t
from turtle import Screen
import random

colors = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
          (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
          (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
          (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95),
          (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

tim = t.Turtle()
tim.color('white')
tim.dot(20)
tim.speed('fastest')
tim.penup()
tim.setpos(-100, -200)
tim.pendown()
t.colormode(255)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setpos(x=-100, y=tim.ycor() + 50)
    tim.pendown()

screen = Screen()
screen.exitonclick()

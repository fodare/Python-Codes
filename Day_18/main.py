"""
Day 18
Intermediate graphical User Interface
"""
import turtle

import colorgram
from color_repo import color_list
import turtle as turtle_module
import random

turtle_module.colormode(255)
t = turtle_module.Turtle()

t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

# rgb_colors = []

# colors = colorgram.extract('image.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

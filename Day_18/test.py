from turtle import Turtle, Screen
import random

t = Turtle()

colour_list = ["blue", "Red", "Orange", "Yellow", "Gray", "brown", "Pink", "Purple"]
direction = [0, 90, 180, 270]


def random_walk():
    for _ in range(200):
        t.setheading(random.choice(direction))
        t.color(random.choice(colour_list))
        t.pensize(5)
        t.speed("fastest")
        t.forward(50)


random_walk()

screen = Screen()
screen.exitonclick()

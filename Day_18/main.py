from turtle import Turtle, Screen
import turtle as t
import random

timmy_turtle = Turtle()
t.colormode(255)

colors = ["Red", "Blue", "Purple", "Yellow", "Green", "Gray", "Brown", "Coral"]
directions = [0, 90, 180, 270]

def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy_turtle.speed("fast")

def draw_spirograph(size_of_gap):
    for _ in range(int (360 / size_of_gap)):
        timmy_turtle.color(random_color_generator())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)

draw_spirograph(8)

screen = Screen()
screen.exitonclick()

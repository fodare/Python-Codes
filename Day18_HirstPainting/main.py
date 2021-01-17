"""Day 18
More of Tuples, importing modules
and GUI's
The Hirst Painting projects"""
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.pu()
tim.hideturtle()
color_list = [(245, 235, 235), (225, 235, 235), (248, 229, 229),
              (231, 245, 245), (122, 180, 180), (198, 173, 173),
              (231, 154, 154), (31, 117, 117), (235, 204, 204),
              (216, 127, 127), (176, 13, 13), (216, 78, 78),
              (26, 144, 144), (11, 172, 172), (209, 63, 63), (237, 75, 75),
              (244, 159, 159), (15, 183, 183), (63, 20, 20), (15, 32, 32),
              (163, 57, 57), (74, 26, 26), (148, 191, 191), (127, 210, 210),
              (20, 47, 47), (103, 116, 116), (171, 21, 21), (247, 159, 159),
              (135, 215, 215), (170, 185, 185)]
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
# screen.screensize(canvwidth=100, canvheight=100, bg=None)
screen.exitonclick()


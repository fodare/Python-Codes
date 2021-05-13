from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

"""
w = forward
s = Backwards
a = counter- clockwise
d = turn clockwise
c = clear screen and set turtle back to origin
"""


def move_forward():
    """Move the turtle forward by 20 spaces"""
    t.forward(20)


def move_backward():
    """Move the turtle backwards by 20 spaces"""
    t.backward(20)


def counter_clockwise():
    """Turns the heading of the turtle by 90 degrees"""
    t.setheading(90)


def move_clock_wise():
    t.setheading(180)


def clear_screen():
    """Clears all of the drawings on the screen
    and restore the turtle to it's initial status"""
    t.clear()
    t.penup()
    t.home()
    t.pd()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=move_clock_wise, key="d")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()

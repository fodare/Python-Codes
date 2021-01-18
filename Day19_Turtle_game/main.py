"""
Day 19. Listening to Keyboard
Strokes
"""
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()  # Create a new Screen instance
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of the turtle which would win the race: ")
print(user_bet)
colors = ["red", "blue", "orange", "green", "purple", "pink"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create multiple turtle
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. The color of the winning turtle is: {winning_color}")
            else:
                print(f"You lose. The color of the winning turtle is: {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

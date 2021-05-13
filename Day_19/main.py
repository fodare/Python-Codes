"""
Day 19

Higher Order function.
Object state and instances
Event listeners, More on turtle Graphics

"""
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# configure the Screen size
screen.setup(height=400, width=500)
# Get user input
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle are you betting on ? Enter a color: ")
colors = ["red", "blue", "yellow", "orange", "purple", "green"]
y_positon = [-70, -40, -10, 20, 50, 80]
runner_list = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positon[turtle_index])
    runner_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for runner in runner_list:
        if runner.xcor() > 230:
            is_race_on = False
            winner = runner.pencolor()
            if winner == user_bet:
                print(f"Jackpot!. You won the bet!. The color of the winning turtle is {winner}")
            else:
                print(f"Sorry! You lost the bet.The color of the winning turtle is {winner}")
        random_distance = random.randint(0, 10)
        runner.forward(random_distance)


screen.exitonclick()

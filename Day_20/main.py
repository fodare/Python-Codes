"""
Day 20
Building Sample snake game to learn more about the Turtle tkinter GUI
"""
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()

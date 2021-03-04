# Day 4
# Randomisation, Python List

import test
import random

images = [test.rock, test.paper, test.scissors]

# Goal: Rock Paper Scissors game

# ToDo 1: Welcome the user to the game and get their input
print("Welcome to the Rock Paper Scissors game")
user_input = int(input(f'What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n'))
if user_input >= 3 or user_input < 0:
    print("You typed the wrong input. Game over!")
else:
    print(images[user_input])

# Todo 2: build game logic
computer_choice = random.randint(0, 2)
print(f'Computer chose: \n{images[computer_choice]}')

if user_input == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_input == 2:
    print("You lose")
elif computer_choice > user_input:
    print("You lose")
elif user_input > computer_choice:
    print("You win")
elif computer_choice == user_input:
    print("It's a draw")

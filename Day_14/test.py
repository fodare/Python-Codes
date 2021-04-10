import random
from game_data import data
from art import logo

score = 0

print(logo)


def compare_question():
    for question_data in data:
        user_guess = input(
            f"Compare A: {question_data['name']}, a {question_data['description']} from {question_data['country']}. ")

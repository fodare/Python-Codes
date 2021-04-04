"""
Day 12
Namespaces local variables and Global variables
"""
# Goal: Number guessing game
import random
answer = random.randint(1, 100)
easy_level = 10
hard_level = 5

def check_answer(guess, answer, turns):
    """Returns the number of turns remain and check the guess value against the answer"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"Correct! The answer is {answer}.")

def set_difficulty():
   level = input("Chose game difficulty level. Type 'hard' or 'easy': \n")
   if level == 'easy':
       return easy_level
   else:
       return hard_level

def game():
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt(s) remaining to guess the correct number")
        guess = int(input("Make a guess: \n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've ran out of attempts. You lost!")
            return
        elif guess != answer:
            print("Guess again.")
game()

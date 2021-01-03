"""
Day 12: Scope, Global and local vraiables and Constants
Goal: Number guessing game.
"""

####### Scope #######
# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside the function: {enemies}")


# increase_enemies()
# print(f"enemies  outside the funtion: {enemies}")


####### Local Scope / Variable #######

# This are variables which are only accesisble to the block
# of code it was defined.


####### Global Scope / Variable #######
# This are the types of variable that are accessible in any
# part of the program


# Note: There are no block scopes


# Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     # This method is not so good. You can use the return
#     # method to do the manipulation then save the value in another variadble
#     global enemies
#     enemies += 1
#     print(enemies)


# increase_enemies()

# Global Constants: They are varibles that their values do not change.
# Constant names are generally written in upper case

####### Game Start #######
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
Logo = """
 ________                            .__                   ________
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/
"""
print(Logo)

# Function to check user's guess against actual answer


def check_answer(guess, answer, turns):
    """ Checks answer against guess and returns the number of turns remaining """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"slam donk The answer was {answer}")

# Function to set game difficulty level


def set_deficulty():
    level = input(f"Chose a difficulty level. Type 'hard' or 'easy': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    print(f"Welcome to my Number Guessing Game !")
    print(f"I'm thinking of a number between 1 and 100.")
    # Random number generator
    answer = randint(1, 100)
    print(f"The actual answer is: {answer}")

    # The number of chaces the user gets based on the difficluty level
    turns = set_deficulty()

    guess = 0
    while guess != answer:
        print(
            f"You have {turns} attempts remaining to guess the correct number")
        # User makes a guess
        guess = int(input(f"Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess. You lose!")
            return
        elif guess != answer:
            print("Guess again.")


game()

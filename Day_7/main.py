# Day 7
# Goal Hangman Project

import random
from ASII import stages
word_list = ["aardvark", "baboon", "camel"]
lives = 6
# ToDo 1: Generate random word
random_word = random.choice(word_list)

# ToDo 2: Generate random word and blank list
random_word = random.choice(word_list)
blanks = []
for letter in random_word:
    blanks.append("_")

# ToDo 3: Gamer_Over Flag
game_over = False

# ToDo 4: Game logic
while not game_over:
    """Get user guess word"""
    user_char = input("Guess a character in the word: \n").lower()
    for position in range(len(random_word)):
        char = random_word[position]
        if char == user_char:
            blanks[position] = char
    if user_char not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    print(blanks)
    if "-" not in blanks:
        game_over = True
    print(stages[lives])
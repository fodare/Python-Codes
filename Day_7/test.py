import random
from ASII import stages

word_list = ["ardvark", "baboon", "camel"]
lives = 6
random_word = random.choice(word_list)
print(random_word)
blanks = []
for letter in random_word:
    blanks.append("-")

game_over = False

while not game_over:
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

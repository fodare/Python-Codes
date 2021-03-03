# Day 3
# Conditional statements, Logical Operators
# Code Block and Scope

# Goal: Treasure Island game

treasure = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
# ToDo 1: Welcome the user
print(treasure)
print("Welcome to the Treasure Island. \nYour Mission is to Find the treasure! ")
# ToDo 2: Print a question
user_input = input(f'You\'re  at a crossed road, where do you turn? Type "left" or "right": \n')
choice_1 = user_input.lower()

# ToDo 3: Get the user's answer and compare.
if choice_1 == "left":
    choice_2 = input(
        'You reach a lake. There\'s an island in the middle of the lake. Type "Wait" to wait for a boat, type "Swim" to swim accross \n').lower()
    if choice_2 == "wait":
        choice_3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose \n").lower()
        if choice_3 == "red":
            print("Room full of fire. Game over!")
        elif choice_3 == "yellow":
            print("You found the treasure. You win!")
        elif choice_3 == "blue":
            print("Room full of snakes.! Game over!")
        else:
            print("Invalid choice. Game over!")

    else:
        print("Game over. You were attacked by a whale. ")
else:
    print("Gamer over. You fell into a hole!")

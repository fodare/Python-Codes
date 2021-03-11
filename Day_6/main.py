# Day 6
# Fuctions, Code Blocks and While loops

# Goal: Escape the Maze game

game_on = True
while game_on:
    user_name = input("What is your name: ")
    if user_name == "Damilare":
        game_on = False
        print("Access Granted!")
    else:
        game_on = False
        print("Nope not correct")


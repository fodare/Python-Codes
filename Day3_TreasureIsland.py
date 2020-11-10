"""
Day 3:
Learnt more on conditional statements.
logical operators, code blocks and scope.
"""

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# check = number % 2
# if check > 0 :
#   print("It's an odd number.")
# else:
#   print("It's an even number.")


# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight / (height * height), 2)
# if bmi < 18:
#   print(f"Your BMI is {bmi}, and you are underweiht")
# elif bmi > 18.5 < 25:
#   print(f"Your BMI is {bmi}, you are of normal weight")
# elif bmi > 25 < 30:
#   print(f"Your BMI is {bmi} and you are overweight")
# elif bmi > 30 < 35:
#   print(f"Your BMI is {bmi} and you are obese")
# elif bmi > 35:
#   print(f"Your BMI is {bmi} and you are clinically obsese")


print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    f"You are at a cross road, where do you want to go? Type 'Left' or 'right': \n").lower()

if choice1 == "left":
    choice2 = input(
        "You have come to a lake. There is an island inn th middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrived at this islan unharmed. There is a house with 3 doord. One red, one yellow and one  blie. which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. Horrah")
        elif choice3 == "blue":
            print("You enter the room full of beasts. Game over")
        else:
            print("You choose a door which does not exist. Game over!")
    else:
        print("You got attacked by a big fish. Game over !")
else:
    print("You fell in a hole. Game over!")


# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

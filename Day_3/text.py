# # ToDO 1: Greet the user
# print("Welcome to the rollercoster height gate!")
#
# # ToDO 2: Get the height of the user and the age
# height = int(input("What is your height in cm?: "))
#
#
# # ToDO 3: Check the height of the user is grater than 120 and their age
# if height >= 120:
#     print(f"You are okay to ride the roller coaster")
#     age = int(input("How old are you: "))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print(f"Your are too short. You need to gain more {120 - height}cm to ride the roller coaster")


# Advance BMI Calculator
# ToDo 1: Get the weight and height of the user
weight = int(input("Enter your weight in Kg: \n"))
height = float(input("Enter your height in Meters: \n"))

# ToDo 2: Calculate the BMI of the user for checking
bmi = round(weight / (height ** 2))
# ToDo 3: print the BMI group the user fall under
if bmi < 18.5:
    print(f"You are underweight. Your BMI is {bmi}")
elif bmi <= 25:
    print(f"You are normal weight. Your BMI is {bmi}")
elif bmi <= 35:
    print(f"You are obese. Your BMI is {bmi}")
elif bmi > 35:
    print(f"You are clinically obese. Your BMI is {bmi}")
# """
# Day 8
# Function with inputs
# End Goal is a Caesar cipher
# Encryption and decryption
# """
# # function are bunch of instructions for the computer to run

# # function with no input or arguments
# # def greet():
# #     print("Hello, How are you")
# #     print("Welcome to the course")
# #     print("Hello world")


# # greet()

# # # function with input / Parameter

# # # data inside the function creation is known as parameter
# # # Parameter is the name of the data thats is been passed in


# # def greet_with_name(userName):
# #     print(f"Hello {userName}")
# #     print(f"Isn't the weather nice today {userName}")


# # # Value in the function call is known as argument
# # # Argument is the actual piece of data that is been used
# # greet_with_name("Damilare")

# # Function with 2 parameters
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")


# greet_with(location="Munster", name="Damilare")

# Day 8 Mini challenge
# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    number_of_cans = (test_h * test_w) / coverage
    number_of_cans = math.ceil(number_of_cans)
    print(f"The number of cans needed is {number_of_cans}")
# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

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
# import math


# def paint_calc(height, width, cover):
#     number_of_cans = (test_h * test_w) / coverage
#     number_of_cans = math.ceil(number_of_cans)
#     print(f"The number of cans needed is {number_of_cans}")
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.


# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number checker

# Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#         if is_prime:
#             print(f"It's a prime number")
#         else:
#             print(f"It's not a prime number")

# # Write your code above this line 👆


# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
    print(f"Here's the {cipher_direction}d result: {end_text}")

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?


# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a new function that calls itself if they type 'yes'.
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 25
    # Try running the program and entering a shift number of 45.
    # Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Closing application. Goodbye")

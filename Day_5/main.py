# Day 5
# For loops, Range and Python Code blocks

# Goal: Simple Password Generator

import random

"""Variables"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

"""Code logic"""
# ToDo 1: Welcome the User to the program
print("Welcome to the Secure Password Generator")
# ToDo 2: Ask the number of letters they would like
nr_letters = int(input("How many letters would you like in your password: \n"))

# ToDo 3: Ask the number of Symbols they would like
user_symbols = int(input("How many symbols would you like in your password: \n"))

# ToDo 4: Ask the number of numbers they would like
num = int(input("How many numbers would you like in your password: \n"))

# ToDo 5: Create password generation logic and print out the password
secure_password = []
for char in range (1, nr_letters + 1):
    secure_password += random.choice(letters)

for sym in range(1, user_symbols + 1):
    secure_password += random.choice(symbols)

for num in range(1, num + 1):
    secure_password += random.choice(numbers)

random.shuffle(secure_password)
password = ""
for char in secure_password:
    password += char
print(f"Your secure password is: {password}")
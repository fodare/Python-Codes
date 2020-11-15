"""
Day 5.
Learning For Loops, Range and code blocks.
"""
# Simple for loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")


# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# # Write your code below this row 👇
# print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# number_student = 0
# for students in student_heights:
#     number_student += 1
# print(number_student)

# avg_height = round(total_height/number_student)
# print(f"The average height of the given student list is {avg_height}")


# # Write your code below this row 👇
# for game in range(1, 101):
#     if game % 3 == 0 and game % 5 == 0:
#         print("FizzBuzz")
#     elif game % 3 == 0:
#         print("Fizz")
#     elif game % 5 == 0:
#         print("Buzz")
#     else:
#         print(game)


# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password:\n"))
nr_symbols = int(input(f"How many symbols would you like:\n"))
nr_numbers = int(input(f"How many numbers would you like:\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for sym in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for num in range (1 , nr_numbers + 1):
#   password += random.choice(numbers)

# print(f"Your password could be: {password}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password could be {password}")

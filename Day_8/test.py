import random

# Functions with parameters

# def print_info(name, location):
#     print(f"The agent name is: {name}")
#     print(f"The agent is located in: {location}")
#
# print_info("Damilare", "Munster Germany")


# ToDo 1: Area calculator
# def calculate_cans(height, width, coverage):
#     number_of_cans = round((height * width) / coverage)
#     print(f"You would need {number_of_cans} of can(s) to paint the wall")
#
# wall_height = int(input("What's the wall height: \n"))
# wall_width = int(input("What's the wall width: \n"))
# coverage_per_can = 5
#
# calculate_cans(height=wall_height, width=wall_width, coverage=coverage_per_can)

# ToDo 2: Prime number checker
user_num = int(input(f"Enter a number: \n"))


def is_prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


is_prime_number(number=user_num)

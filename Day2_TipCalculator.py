# """
# Learn more about Data types,
# Numbers, Operations,
# Type conversion and f-srings

# End of the day is a Tip calculator.
# """

# # Data Types

# # String

# name = "hello"
# print(type(name))

# # Integer - Whole number without any decimal value and quatations

# unitPrice = 10
# sellingPrice = 20
# price = unitPrice - sellingPrice
# print(price)


# # float. simply numbers with decimal values

# bread = 12
# butter = 5
# meal = bread / butter
# print(meal)  # float data type

# # Boolean. Evalaute to either True / False

# a = 20
# b = 10

# if a > b:
#     print("True")
# else:
#     print("False")


# # Type conversion
# userName = len(input("What is your name: "))
# newUserName = str(userName)
# print("Thank you, your username is " + newUserName + " characters long")

# # Tip to round off decimal number. Use the round method and // for floor method. It chops off the decimal point from a division

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the tip calculator.")
bill = float(input("what is the total bill $: "))
tip_percentage = float(
    input("What percentage tip would you like to give (10,12,15): "))
number_eaters = int(input("How many people to split the bill: "))
bill_with_tip = (tip_percentage / 100 * bill + bill) / number_eaters
final_amout = round(bill_with_tip, 2)
print(f"Bill per person is {final_amout}. Thank you for dinning with us")

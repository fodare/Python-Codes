# Day 10
#
# Functions with outputs

# Goal: Text based calculator APP
from code_resource import logo as cal


# *************** Functions ***************
# Addition
def add(n1, n2):
    """Returns the addition of 2 int inputs"""
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    """Returns the subtraction of 2 int inputs"""
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    """Returns the multiplication of 2 int inputs"""
    return n1 * n2


# Division
def divide(n1, n2):
    """Returns the division of 2 int inputs"""
    return n1 / n2


# *************** Functions dictionary ***************
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(cal)
print("Welcome to the text based calculator!")


def calculator():
    num1 = int(input("What's the first number: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        num2 = int(input("What's the second number: "))
        operation_symbol = input("Type in the Operation from the list above: ")
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

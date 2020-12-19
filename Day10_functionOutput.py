"""
Day 10 fuction with output
function that returns output
Final goal is simple text calculator
"""

# Function with output example

# Function below takes input first name and last name
# then use the title function to format them for output


# def format_name(fname, lanme):
#     formatted_fname = fname.title()
#     formatted_lname = lanme.title()
#     return(f"The formatted First name is: {formatted_fname} and the formatted last name is: {formatted_lname}")


# print(format_name("damilare", "BoSUN"))


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(f"{logo}\n welcome to my simple Calculator.\n please follow the instruction below. ")

# Calculators

# Addition


def add(num1, num2):
    return num1 + num2

# Subtraction


def subtract(num1, num2):
    return num1 - num2

# Multiplication


def multiply(num1, num2):
    return num1 * num2

# Division


def divide(num1, num2):
    return num1 / num2


def modulus(num1, num2):
    return num1 % num2


operation_list = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "%": modulus
}


def calculator():
    input1 = float(input("Enter first number: "))
    for symbol in operation_list:
        print(symbol)

    should_continue = True

    while should_continue:
        select_symbol = input("Type in the operation from the symbol above: ")
        input2 = float(input("Enter next number: "))

        calc_function = operation_list[select_symbol]
        answer = calc_function(input1, input2)
        print(f"{input1} {select_symbol} {input2} = {answer}")

        if input(f"Type 'y' to continue calculation and 'n' to start new calculation:  ") == "y":
            input1 = answer
        else:
            should_continue = False
            calculator()


calculator()

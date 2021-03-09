# ToDo 1: Fuctions
def print_hello():
    print("This function prints hello!")
print_hello()

# Arguments are set of data passed into a function during function call.
# Parameters are set of variables created at the time of a function definition

def welcome_message(user_name):
    print(f"Welcome {user_name}!")

welcome_message("Damilare")

fruits = ["apple", "banana", "cherry"]
def print_fruits(food):
    for x in food:
        print(f"Fruit name:{x}")

print_fruits(fruits)
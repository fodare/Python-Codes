# Python Variables are created when a value is added to it. Example below:
x = 5
y = 10
print(x, y)
userName = "Damilare"
print(userName)

# As python has no command for declaring a varible , it's not necessary to use the var keyword
# Global Variables are varibles created outside a function call. Example below.

# Declaring a global variable.
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# A variable created in a function can only be used in the fuction.
# such type of fuctions are called local functions are are restricted to only where they are created.
# It's as well possible to create a global variable inside the function. This can be done by using
# the global keyword in the varible declaration. Example below


def function2():
    global z
    z = "Global function testing"


function2()

print(z)

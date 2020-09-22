"""
Python does have 3 types of numeric numbers.
They are  mainly:
1: Numbers.
2: float.
3: complex.
"""
import random
x = 10
y = 11.20
z = 1j

print(type(x))
print(type(y))
print(type(z))

# It is also possible to make type conversion in python It's done this way

a = 10  # Number
# Converting a to a float
b = float(a)
print(type(b))

# The method is also applicable to converting from float to int and fron int to float. But we can not
# from complex numeric datatype to int / float.
# Python does not have a random () method to generate a random number but you can import random into the
# python project

print(random.randrange(1, 10))

# String Methods
# To get the length of a string in python, you use the len() method. Example below
c = "Hello World!"
d = len(c)
e = "The length of the string is {}"
print(e.format(d))

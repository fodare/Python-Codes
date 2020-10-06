"""
Python conditional Statement.
if, Elif, else statements
"""
a = 33
b = 300
if b > a :
    print("b is grater than a")
print("*****************")

"""
Elif checks if the first if condition is not satisfiled
or need to check for more condition. 
"""

c = 40
d = 21
if d > c :
    print("d is grater than c")
elif d < c :
    print("d is lesser than c")

print("***************")

"""
else statement
So if none of the conditions in if and Elif are not caught then
it comes in in the else statement
"""
e = 21
f = 22
if e == f :
    print("e and f are equal")
elif f < e :
    print("f is grater than e")
else :
    print("none of the condition is statisfied")
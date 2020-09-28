"""
Conditional Statements are  statemnt used to perfom Logical operations.
Example is the if statements. Example below:
"""

a = 20
b = 10
if b > a:
    print("B is grater than a")
else:
    print("A is greater than b")

"""
Th Elif is used when the first if statemnent is not true.
Basically Elif is the python version of else if
 Example below:
"""
c = 20
d = 20
if d > c:
    print("D is greater than C")
elif c == d:
    print("C and D are equal")
else:
    print("C is greater than d")

"""
The else statement is designed to catch a condition that is not with the scope.
Example above.
"""
"""
Combining Logical operators with conditional statement. example below:
And operator : both conditions needs to be statisfied.
"""
e = 200
f = 33
g = 500
if e > f and g > e:
    print("Both conditions are true.")

"""
or operator : At least 1 of the condition needs to be satisfied.
"""
h = 200
i = 33
j = 500
if h > i or h > j:
    print("At least one of the condition is true")


"""
Another concept is the nested if statemnt. This means and if statemnt inside another if statement.
Example below:
"""
k = 41

if k > 10:
    print("K is greater than 10")
    if k > 20:
        print("K is also greater than 20")
    else:
        print("K is not greater than 20")

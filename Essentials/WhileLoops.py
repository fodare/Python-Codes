"""
Python has 2 primite looping statements. They are namely:
while loops.
for loops
"""
"""
While loops will keep running as long as the condition is true.
Example below would print the value of i as long as the condition is true.
"""

i = 1
while i < 6:
    print(i)
    i += 1

"""
The Break statemnt is used to stop the execution of while loop
even if the condition is true. Example Below:
"""
j = 0
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

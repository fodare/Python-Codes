"""
Python While Loops
Use to exceute conditional statement as long as 
a given condition is true.
"""
# i = 1
# while i < 6:
#     print(i)
#     i+=1


"""
The break statement is used to stop the loop 
when a certain condition is satisfied.
"""
# i = 2
# while i < 10 :
#     print (i)
#     if i == 3:
#         break
#     i += 1

"""
Another function is the continue keyword
checks for a condition then continues with 
the loop
"""
# i = 1 
# while i < 10 :
#     i += 1
#     if i == 3 :
#         continue
#     print(i)


"""
You can as well add the else clause if the condition  is not satisfied. 
"""
i = 1
while i < 10 :
    print(i)
    i += 1
    
else:
    print("i is no longer lesser than 10")
# For Loop
# ToDo 1: Looping through a list
# fruits = ["Apple", "PEach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# ToDo 2: Calculate Average height
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# height_sum = 0
# list_len = 0
#
# for i in student_heights:
#     list_len = list_len + 1
#
# for height in student_heights:
#     height_sum = height + height_sum
#
# print(f"The avg height is: {round(height_sum / list_len)}")

# ToDo 3: Print the highest score
# You can also use the max() function or min()
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 2000]
# highest_score = 0
#
# for score in student_scores:
#     if highest_score < score:
#         highest_score = score
#     else:
#         highest_score = highest_score
# print(f"The highest score in the class is: {highest_score}")

# ToDo 4: Print the total number of value between a range
# total = 0
# # start, end, steps
# for number in range(1, 101, 2):
#     total += number
# print(total)

# ToDo 5: Print FizBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

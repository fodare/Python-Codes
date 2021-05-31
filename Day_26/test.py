import random
"""
List Comprehension
"""
scores = [1, 2, 3]
"""
New_list_name = [operation for each_item in stored list]
"""
new_scores = [score + 1 for score in scores]
print(new_scores)



"""
Conditional list comprehension

new_list = [new_item for item in list if test]
"""
names = ["damilare", "spade", "james", "dave", "dirk"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)


# ToDo 1 : Test 1 - print out the squared vlaues in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number = [num**2 for num in numbers]
print(squared_number)

# ToDo 2 : Test 1 - Print out the even numbers from the list
all_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in all_numbers if num % 2 == 0]
print(even_numbers)


"""
Dictionary comprehension
new_dict = {new_key:new_value for item in list}
new_dict = {new_key: new_value for (key,value) in dict.items()}
"""
student_names = ["Alex", "George", "James", "Jhon", "Biyi"]
student_scores = {student : random.randint(1, 100) for student in student_names}
print(student_scores)
passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_student)
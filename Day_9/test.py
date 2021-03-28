'''Dictionary'''
#
# # Creating a Python Dictionary
# programming_dictionary = {
#     "bug": "An error in a program that prevents the program  from running as expected",
#     "function": "A piece of code that you can eaily call over and over again.",
# }
#
# # Retrieving data from a python dictionary
# print(programming_dictionary["function"])
# print("*****************************************")
#
# # Adding new Key-value pair to a dictionary
# programming_dictionary["loop"] = "Continuous execution of a block of code until a condition is satisfied"
# '''You can also use the method to editing an existing value '''
# print(programming_dictionary)
# print("*****************************************")
#
# # Looping through a dictionary
# for key in programming_dictionary:
#     print(f"{key}: {programming_dictionary[key]}")


# Todo 1: Create a grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grade = {}


def print_grade(score_list):
    for student in score_list:
        score = student_scores[student]
        if score > 90:
            student_grade[student] = "Outstanding"
        elif score > 80:
            student_grade[student] = "Excellent"
        elif score > 70:
            student_grade[student] = "Very good"
        else:
            student_grade[student] = "Failed class"
    print(student_grade)


print_grade(score_list=student_scores)

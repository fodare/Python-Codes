# """
# Dictonary concept in Python.
# Like some sort of Key -  value concept
# Whn the Key is the identificatiion name and the
# value is an attribute of the key.

# Python Dictionary i created by: Dictionary name = [Key:value]
# Example below:
# name = ["User1": "Damilare", "User2": "Olatunbosun", ....]
# """
# # programming_dictionary = {
# #     "Bug": "An error in a program that prevents the program from running as expected.",
# #     "Function": "A piece of code that you can easily call over and over again.",
# #     "Loop": "The process of running a condition over and over untill it's stopped",
# # }
# # print(programming_dictionary["Loop"])

# # # Adding to a dictionary
# # programming_dictionary["Variable"] = "A container which is used to store temporary value for later use."
# # print(programming_dictionary)


# # # clearing a dictionary / wipe a dictionary
# # """
# # Dictionary_name = {}
# # """
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Example test
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)
import console
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# HINT: You can call clear() to clear the output in the console.
print(f"{logo}\n Welcome to the Blind bidder app. Shall we ? \n")
blind_bidders = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid amount {highest_bid}")


while not bidding_finish:
    bidder_name = input(f"Please enter your name: ")
    bidder_price = int(input(f"Please enter your bid price $: "))
    blind_bidders[bidder_name] = bidder_price
    should_contine = input(
        f"Are there any other bidders? Type 'yes' or 'no': ")
    if should_contine == "no":
        bidding_finish = True
        find_highest_bidder(blind_bidders)
    elif should_contine == "yes":
        console.clear()

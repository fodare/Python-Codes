# Day 2
# Data types, Numbers, Operations
# Type Conversion and F strings

# Goal: Tip Calculator

# ToDO 1: Welcome the User
print("Welcome to the Tip Calculator \n")
# ToDO 2: Collect the total bill amount
total_bil = float(input("What was the total bill? $: "))
# ToDO 3: Collect the percentage of the Tip amount
tip = int(input("What percentage tip would you like to give? (10, 12 or 15): \n"))
# ToDO 4: Collect the number of people who are going to split the bill
num_people = int(input("How many number of people to split the bill?: \n"))
# ToDo 5: Print the amount for each person
tip_as_percentage = tip / 100
total_tip_amount = total_bil * tip_as_percentage
final_bill = total_bil + total_tip_amount
bill_per_person = final_bill / num_people

print(f"Each person pays$: {bill_per_person}")
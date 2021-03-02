# Numbers are of the data-types  Integers

# TODo: 1 Collect the name of the user get the length in numbers
# num = len(input("What is your name: \n"))

# TODo: 2 convert the length of the name to a string to be used later
# new_num = str(num)

# TODo: 3 Concatinate the new string number with a String using the f String
# print(f"The length of your name is {new_num} :)")

# Sample Test 1

# two_digit_number = input("Enter a twi digit number: \n")
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# added_number = (num1 + num2)
# print(f"The addition of the two numbers are: {added_number}")


# Sample Test 2 (BMI Calculator)
print("Welcome to the BMI Calculator!")
weight_kg = int(input("What is your weight in Kg: \n"))
height_meters = float(input("What is your height in meters: \n"))
bmi = weight_kg / (height_meters ** 2)
print(f"Your BMI is: {round(bmi)}")

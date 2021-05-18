"""
Day 22 -

File manipulation in python
How to open a file with different modes and
How to write to a file.
File paths (Relative and Absolute)
"""

PLACEHOLDER = "[name]"

#Todo: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# replace the [name] placeholder with the actual name.
# save the letter in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", mode="r") as friend_list:
    names = friend_list.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as compleated_letter:
            compleated_letter.write(new_letter)
    print("Successfully generated letters ")



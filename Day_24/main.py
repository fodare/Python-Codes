"""
Day 24
File handling and manipulations
"""
# To open a file (Open Method)
# with open("my_file.txt", mode="r") as file:
#     file_content = file.read()  # Reads the content of the file
#     file_content = file.append("New message")
#
# print(file_content)

# # To write to a file (Write Method)
# with open("my_file.txt", mode="w") as file:
#     file.write("New content written into file")
# print(file)


# To append / added more content to a file
with open("my_file.txt", mode="a") as file:
    file.write("\n this was done with the append method")



"""
Sample was to open and close a file
"""
# secret_text = open("secret.txt")
# contents = secret_text.read()
# print(contents)
# secret_text.close()

"""
Another way to open and close a file
"""
with open("secret.txt") as spy_message:
    contents = spy_message.read()
    print(contents)

"""
Sample way to write to a file
"""
with open("secret.txt", mode="a") as spy_ping:
    spy_ping.write("\nThis is a new message")

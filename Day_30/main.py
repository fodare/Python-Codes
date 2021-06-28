"""
Day 30
Exception handling
"""

"""
The four main principle of exception handling.

    1: Try block - Something that might cause and exception.
    2: Except block - action to be performed when there is an exception.
    3: else block - if there were no exceptions.
    4: finally block - execute no matter what happens
    5: raise - raising our own exceptions. Meaning a custom exception
    
Example below.
"""
try:
    file = open("test_file.txt")
    sample_dictionary = {"key": "value"}
    print(sample_dictionary["key"])
except FileNotFoundError:
    file = open("test_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("Just messing with your code!")

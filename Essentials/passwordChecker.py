"""
Simple Password checker
"""
username = input("Enter your desired username: ")
password = input("Enter a pssword: ")

passwordLength = len(password)
hiddenPassword = '*' * passwordLength

if passwordLength > 10:
    print(
        f'Hello {username}, your password {hiddenPassword}  is {passwordLength} characters long')
else:
    print(f'Your password is too short')

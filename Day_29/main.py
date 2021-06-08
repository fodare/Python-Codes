from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #     password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_name = web_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Field", message="Please do not leave and field empty!")
    else:
        is_okay = messagebox.askokcancel(title={website_name},
                                         message=f"These are the creds entered \n {website_name}, {email}, {password}\n Correct ? ")

    if is_okay:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website_name} | {email} | {password}\n")
        # user_name_entry.delete(0, END)
        web_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        messagebox.showinfo(message="Canceling Error")


# ---------------------------- UI SETUP ------------------------------- #
"""Creating Window """
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

"""Creating canvas"""
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

""" Website Area """
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

""" Email/Username """
user_name = Label(text="Username/Email:")
user_name.grid(row=2, column=0)

user_name_entry = Entry(width=35)
user_name_entry.insert(0, "dummy.email@hotmail.com")
user_name_entry.grid(row=2, column=1, columnspan=2)

""" Password """
user_password = Label(text="Password:")
user_password.grid(row=3, column=0)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

""" Generate Password button """
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

""" Add Password """
add_pass = Button(text="Add", width=30, command=save_pass)
add_pass.grid(row=4, column=1)

window.mainloop()

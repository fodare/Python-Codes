from tkinter import *

"""
Creating windows and Labels in Tkinter
"""
window = Tk()
window.title("My first Python GUI program")
window.minsize(width=500, height=300)
window.config(padx = 100, pady = 100)

"""Creating a label"""
my_label = Label(text="This is a label: ", font=("monospace", 12))
my_label.grid(column = 0, row = 0)
"""Setting component options """
my_label.config(text="New text:")

"""Creating buttons"""
def button_clicked():
    input_text = input.get()
    my_label.config(text = input_text)

button = Button(text="click me", command=button_clicked)
button.grid(column = 1, row = 1)

"""Creating Input"""
input = Entry(width = 50)
input.grid(column = 2, row = 1)





window.mainloop()  # Keeps the window looping so it does not close

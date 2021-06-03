"""
Day 27
Graphical User Interfaces with tkinter  and function arguments
"""
from tkinter import *

window = Tk()
window.title("Miles to Km calculator")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def calculate_km():
    miles_data = input_data.get()
    miles_to_km = round(int(miles_data) * 1.6)
    output.config(text=miles_to_km)
    return miles_to_km


# Miles entries
input_data = Entry(width=10)
input_data.grid(column=1, row=0)

# Miles labels
input_label = Label(text="Miles")
input_label.grid(column=2, row=0)

# Output labels
output_label = Label(text="is equal to: ")
output_label.grid(row=3, column=0)

# output value
output = Label(text="")
output.grid(row=3, column=1)

# Km label
km_lablel = Label(text="Km")
km_lablel.grid(row=3, column=3)

# Calculate Button
button = Button(text="Calculate", command=calculate_km)
button.grid(row=4, column=1)

window.mainloop()

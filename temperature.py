import tkinter as tk 
from tkinter import ttk

def convert():
    num = int(number.get())

    if con_var.get() == 1: # Celsius to Fahrenheit
        result = (num * 9/5) + 32
        result_1.config(text = f"{num}C is equal to {result}F")

    elif con_var.get() == 2: # Fahrenheit to Celsius
        result = (num - 32) * (5/9)
        result_1.config(text = f"{num}F is equal to {result}C")

root = tk.Tk()
con_var = tk.IntVar()

title = ttk.Label(root, text = "Temperature\nConverter")
title.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

number = ttk.Entry(root)
number.grid(row = 1, column = 0, columnspan = 2)

c_to_f_rb = ttk.Radiobutton(root, text = "C to F", variable = con_var, value = 1)
c_to_f_rb.grid(row = 2, column = 0)

f_to_c_rb = ttk.Radiobutton(root, text = "F to C", variable = con_var, value = 2)
f_to_c_rb.grid(row = 2, column = 1)

convert_b = ttk.Button(root, text = "Convert", command = convert)
convert_b.grid(row = 3, column = 0, columnspan = 2 )

result_1 = ttk.Label(root, text = "")
result_1.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()
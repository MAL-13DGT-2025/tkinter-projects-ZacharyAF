import tkinter as tk 
from tkinter import ttk


title = tk.Label(root, text = "Calculator")

root = tk.Tk() # MUST HAVE
root.title("Calculator")

calc = ttk.Entry(root)
calc.grid(row = 0, column = 0, columnspan = 4)

b_7 = ttk.Button(root, text = "1")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "2")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "3")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "4")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "5")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "6")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "7")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "8")
b_7.grid(row = 1, column = 1)

b_7 = ttk.Button(root, text = "9")
b_7.grid(row = 1, column = 2)

b_7 = ttk.Button(root, text = "/")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "*")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "-")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "+")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "=")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "0")
b_7.grid(row = 1, column = 0)

b_7 = ttk.Button(root, text = "AC")
b_7.grid(row = 1, column = 0)



root.mainloop()


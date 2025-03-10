import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Rock Paper Scissors")

choice = tk.StringVar()

choice = ttk.Entry(root, textvariable = choice)
choice.grid(row = 1, column = 0, columnspan = 3)

title = ttk.Label(root, text = "Rock,\nPaper,\nScissors,")
title.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 10)

rock_1 = ttk.Button(root, text = "Rock", command = lambda:press("Rock"))
rock_1.grid(row = 2, column = 0)

paper_2 = ttk.Button(root, text = "Paper", command = lambda:press("Paper"))
paper_2.grid(row = 2, column = 1)

scissors_3 = ttk.Button(root, text = "Scissors", command = lambda:press("Scissors"))
scissors_3.grid(row = 2, column = 2)

label = ttk.Label(root, text = "")
label.grid(row = 3, column = 0, columnspan = 3, padx = 50, pady = 10)



root.mainloop()
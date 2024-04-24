import tkinter as tk

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the result
entry = tk.Entry(root, width=20, borderwidth=7)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

# Create buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=25, pady=25, command=lambda char=text: button_click(char))
    button.grid(row=row, column=column)

# Clear button
clear_button = tk.Button(root, text="CLEAR", padx=25, pady=25, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Backspace button
backspace_button = tk.Button(root, text="⌫", padx=30, pady=25, command=backspace)
backspace_button.grid(row=5, column=2)

# Calculate button
calc_button = tk.Button(root, text="=", padx=30, pady=30, command=calculate)
calc_button.grid(row=5, column=3)

root.mainloop()

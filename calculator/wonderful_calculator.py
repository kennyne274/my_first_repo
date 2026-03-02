import tkinter as tk

# wonderful calculator"

"""Using eval() is not recommended for security reasons in production code,
    but this is a simple learning project calculator, so we use it for simplicity."""
    

# Insert number or operator into the entry field
def num_click(value):
    entry.insert(tk.END, value)

# Clear the entry field
def clear():
    entry.delete(0, tk.END)

## Evaluate the expression and show result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("calculator")
root.configure(bg="#2D2D2D")

entry = tk.Entry(root, justify="right", width=30, bg="ivory", font=('', 16, 'bold'))
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=5)



buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','+','='
]

row = 1  # Start row 
col = 0  # Start column

# Create and place buttons
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text= button, font=('', 15, 'bold'), 
                        bg="#464545", width=7, height=3, command=calculate)
        btn.grid(row=row, column=col, padx=3, pady=3)
    elif button == "C":
        btn = tk.Button(root, text= button, font=('', 15, 'bold'), 
                        bg="#464545", width=7, height=3, command=clear)
        btn.grid(row=row, column=col,  padx=3, pady=3)
    else:
        btn = tk.Button(root, text= button, font=('', 15, 'bold'),
                        bg="#464545", width=7, height=3, command=lambda v=button: num_click(v))
        btn.grid(row=row, column=col,  padx=3, pady=3)
    
    col += 1
    if col > 3:
        col = 0
        row += 1
    
root.mainloop()

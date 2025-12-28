# pretty calculator

from tkinter import *


def clicked(digit):
    if digit == "<":
        entry.delete(len(entry.get())-1)
    else:
        entry.insert(END,digit)

def del_digit():
    entry.delete(0, END)
    label.config(text = "")

def calculate():
    try:
        result = eval(entry.get())
    except:
        label.config(text="ERROR")
    else:
        label.config(text = result)


root = Tk()
root.title("계산기")
root.resizable(0,0)
root.config(padx=10, pady=10, bg="#BBEBE0")
digits=[
    ["7","8","9","*"],
    ["4","5","6","/"],
    ["1","2","3","-"],
    ["0",".","←","+"]
]
entry = Entry(root, width=25, font=("Courier",15,"bold"), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=5)
entry.focus()
label = Label(root, text="", width=25, bg="aliceblue",font=("Courier",15,"bold"))
label.grid(row=1, column=0, columnspan=4, pady=5)
for r in range(4):
    for c in range(4):
        digit=digits[r][c]
        button = Button(root, text=digit, width=5, font=("Courier",15,"bold"), bg="lightblue", command=lambda x =digit: clicked(x))
        button.grid(row=r+2,column=c, pady=2)

clear_button = Button(root, text="C", width=10, font=("Courier",15,"bold"), bg="cyan", command= del_digit)
clear_button.grid(row=6, column=0, columnspan=2, pady=3)
cal_button = Button(root, text="=", width=10, font=("Courier",15,"bold"), bg="cyan", command=calculate)
cal_button.grid(row=6, column=2, columnspan=2, pady=3)
root.mainloop()

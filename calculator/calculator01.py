# A simple calculator

import tkinter as tk
from tkinter import messagebox

FONT=("Courier", 10,"bold")

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "+":
            result = num1+num2
        elif op == "-":
            result = num1-num2
        elif op == "*":
            result = num1*num2  
        elif op == "/":
            if num2 == 0:
                label.config(text="0으로 나눌 수 없습니다.")
                return 
            result = num1/num2 
           
        label.config(text=f"{result:.2f}")
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter it correctly."
        )

        
root = tk.Tk()
root.title("미니 계산기")
root.geometry("380x480")
root.configure(bg="lightblue")
root.resizable(False, False)

top_space = tk.Frame(root, height=30, bg="lightblue")
top_space.pack()

tk.Label(root, text="첫번째 숫자 입력", font=FONT,bg="lightblue").pack()
entry1 = tk.Entry(root, font=("Courier", 15,"bold"), width=20)
entry1.pack(pady=5)
tk.Label(root, text="두번째 숫자 입력", font=FONT,bg="lightblue").pack()
entry2 = tk.Entry(root, font=("Courier", 15,"bold"), width=20)
entry2.pack(pady=5)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=(20,10))

tk.Button(button_frame,text="+", width=5,command=lambda: calculate("+"),font=FONT,bg="lightpink").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="-", width=5,command=lambda:calculate("-"),font=FONT,bg="lightpink").grid(row=0, column=1, padx=5)
tk.Button(button_frame,text="*", width=5,command=lambda:calculate("*"),font=FONT,bg="lightpink").grid(row=0, column=2, padx=5)
tk.Button(button_frame,text="÷", width=5,command=lambda:calculate("/"),font=FONT,bg="lightpink").grid(row=0, column=3, padx=5)
label = tk.Label(root,text="",font=("Courier", 15, "bold"),bg="ivory", fg="navy",width=20)
label.pack()
root.mainloop()

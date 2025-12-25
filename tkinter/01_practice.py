# # Creating a Checkbutton (Practice)

import tkinter as tk
from tkinter import messagebox

def check_status():
    if chk.get() ==0:
        messagebox.showinfo("", "Checkbutton deselected")
    else:
        messagebox.showwarning("","Checkbutton selected")

root = tk.Tk()
root.title("Practice")
root.geometry("300x250")
root.resizable(0,0)

chk = tk.IntVar()

cb = tk.Checkbutton(root, text="Click here", variable=chk, command=check_status)
cb.pack(pady=30)
root.mainloop()

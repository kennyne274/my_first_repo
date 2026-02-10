# Simple Digital Clock 

from tkinter import*
from datetime import datetime

root = Tk()
root.title("MY Clock")

def time():
    now = datetime.now()
    str = now.strftime("%H:%M:%S %p")
    label.config(text=str)
    label.after(1000, time)

label = Label(root, bg="black", fg="cyan", font=("Times New Roman", 60), padx=20, pady=20)
label.pack()

time()
mainloop()

# Simple Digital Clock 

from tkinter import*
from datetime import datetime

# Create the main window
root = Tk()
root.title("MY Clock")

# Create and configure the time display label
def time():
    now = datetime.now()
    str = now.strftime("%H:%M:%S %p")
    label.config(text=str)
    label.after(1000, time)

# Center the label in the window
label = Label(root, bg="black", fg="cyan", font=("Times New Roman", 60), padx=20, pady=20)
label.pack(expand=True)

# Start the clock
time()
mainloop()

# Simple Digital Clock 

import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.date_label = tk.Label(root, font=("New Roman Times", 20), fg = "yellow", bg="#000000")
        self.date_label.pack(expand = True, fill='both')
        self.label = tk.Label(root, font=("New Roman Times", 50), fg = "cyan", bg="#000000")
        self.label.pack(fill='x')
        self.update_clock()

    def update_clock(self):
        current_date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S")
        self.date_label.config(text=current_date)
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("320x170")
    root.resizable(False, False)

    clock = DigitalClock(root)
    root.mainloop()
        


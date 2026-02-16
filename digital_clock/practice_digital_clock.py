# Simple Digital Clock 

import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.configure(bg="red")
        self.root.attributes("-topmost", True)
        font_time = ("Times New Roman", 50)
        font_date = ("Times New Roman", 20)
        try:
            font_time = ("DS-Digital", 50, "bold")
            font_date = ("DS-Digital", 20, "bold")
        except tk.TclError:
            pass
        self.date_label = tk.Label(root, font=font_date, fg = "yellow", bg="#000000")
        self.date_label.pack(fill='x', pady=(0,2))
        self.label = tk.Label(root, font=font_time, fg = "cyan", bg="#000000")
        self.label.pack(expand=True, fill='both', pady=(0,2))
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
        

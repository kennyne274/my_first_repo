"""
Beautiful Digital Clock
You need to download the 'DS-Digital' font for the best look, 
but if it's not available, it will automatically fall back to Courier font.
For the best visual effect, download and install the **DS-Digital** font:  
[Download DS-Digital font here](https://www.dafont.com/ds-digital.font)
Enjoy your time! :)
"""

import tkinter as tk
import time


# Main window
root = tk.Tk()
root.title("Digital Clock with Date & Day")
root.geometry("640x300")
root.configure(bg="#1c1c1c")
root.resizable(False, False)


# Clock update function
def clock():
    try:
        now = time.localtime()

        # date
        date_label.config(text=time.strftime("%Y.%m.%d", now))
        # day of the week
        day_label.config(text=time.strftime("%a", now))
        # AM/PM
        ampm_label.config(text=time.strftime("%p", now))
        # time (24-hour format)
        time_label.config(text=time.strftime("%H:%M:%S", now))
    except Exception as e:
        time_label.config(text="ERROR", fg="red")
        print(f"Clock update error: {e}")

    # Update every 200 milliseconds
    root.after(200, clock)


# Font settings
# Try to use DS-Digital font first, fallback to Courier if not available
try:
    FONT_TIME = ("DS-Digital", 75, "bold")
    FONT_TOP  = ("DS-Digital", 25, "bold")
except:
    FONT_TIME = ("Courier", 75, "bold")
    FONT_TOP  = ("Courier", 25, "bold")


# Outer frame (border)
outer = tk.Frame(root, bg="#2b2b2b", bd=1, relief="solid")
outer.pack(expand=True, fill="both", padx=15, pady=15)


# Top frame for date, day, AM/PM
top_frame = tk.Frame(outer, bg="#1a1a1a")
top_frame.pack(fill="x", padx=10, pady=(10, 5))

# Labels for AM/PM, Day, Date
ampm_label = tk.Label(top_frame, font=FONT_TOP, fg="red",    bg="#1a1a1a", width=10)
day_label  = tk.Label(top_frame, font=FONT_TOP, fg="yellow", bg="#1a1a1a", width=10)
date_label = tk.Label(top_frame, font=FONT_TOP, fg="white",  bg="#1a1a1a", width=12)

ampm_label.grid(row=0, column=0, padx=5, pady=5)
day_label.grid(row=0, column=1, padx=5, pady=5)
date_label.grid(row=0, column=2, padx=5, pady=5)


# Time display frame
time_frame = tk.Frame(outer, bg="#1a1a1a")
time_frame.pack(expand=True, fill="both", padx=10, pady=(5, 10))

# Main time label
time_label = tk.Label(
    time_frame,
    font=FONT_TIME,
    fg="#00ffff",  
    bg="#1a1a1a"
)
time_label.pack(expand=True)


# Start the clock
clock()

root.mainloop()

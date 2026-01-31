# Python Stopwatch (GUI)
# A simple, nice stopwatch GUI built with Python and Tkinter.

import tkinter as tk
import time


start_time= 0
elapsed_time = 0 
running = False


def format_time(seconds):
    """
    Format total seconds into MM:SS:CC (minutes:seconds:centiseconds)
    """
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    cs = int((seconds - int(seconds)) * 1000//10)
    return f"{minutes:02}:{sec:02}:{cs:02}"

# Start the stopwatch.
def start():
    global running, start_time, elapsed_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update()


def stop():
    global running, start_time, elapsed_time
    running = False
    elapsed_time = time.time() - start_time


def reset():
    global running, start_time, elapsed_time
    running = False
    start_time = 0
    elapsed_time = 0
    time_label.config(text="00:00:00")


def update():
    global running, elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        time_label.config(text=format_time(elapsed_time))
        root.after(10, update)

root = tk.Tk()
root.title("Stopwatch")
root.geometry("500x300")
root.configure(bg="black")
root.resizable(False, False)


# title
title_label = tk.Label(
    root,
    text="StopWatch",
    font=("Times New Roman", 25, "bold"),
    fg="white",
    bg="black"
)
title_label.pack(pady=15)

# Time frame
time_frame = tk.Frame(
    root,
    bg="black",
    highlightbackground="white",
    highlightthickness=3
)
time_frame.pack(pady=10)

# # Time display label
time_label = tk.Label(
    time_frame,
    text="00:00:00",
    font=("Times New Roman", 48, "bold"),
    fg="white",
    bg="black",
    padx=30,
    pady=10
)
time_label.pack()


# buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

# Common button style
btn_style = {
    "font": ("Times New Roman", 12, "bold"),
    "width": 8,
    "pady" : 7,
    "bg": "#e6e6e6",
    "relief": "raised"
}

start_btn = tk.Button(button_frame, text="START", **btn_style, command=start)
stop_btn  = tk.Button(button_frame, text="STOP", **btn_style, command=stop)
reset_btn = tk.Button(button_frame, text="RESET", **btn_style, command=reset)
close_btn = tk.Button(button_frame, text="CLOSE", **btn_style, command=root.destroy)

start_btn.grid(row=0, column=0, padx=5)
stop_btn.grid(row=0, column=1, padx=5)
reset_btn.grid(row=0, column=2, padx=5)
close_btn.grid(row=0, column=3, padx=5)


root.mainloop()

import tkinter as tk
import winsound

# A simple and clean timer - good for basic project or Pomodoro sessions
# Enter an integer (seconds) in the input field and click START to begin countdown

# Requirements
"""
- Python 3.x
- Tkinter (usually included)
- winsound (Windows only — for beep sound)

On macOS/Linux, you can remove or comment out the `winsound.Beep()` lines.
"""

def start_timer():
    try:
        global time_left
        time_left = int(entry.get())
        winsound.Beep(568, 300) # short beep to confirm start
        count_down()
    except ValueError:
        text="Enter an integer only"
        entry.delete(0, tk.END)
        entry.insert(0, text)

def count_down():
    global time_left

    if time_left > 0:
        hours = time_left // 3600
        minutes = (time_left // 60) % 60
        seconds = time_left % 60

        label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        time_left -= 1
        window.after(1000, count_down)   
    else:
        winsound.Beep(568, 300) # beep when time is up
        label.config(text="Time's UP!")


window = tk.Tk()
window.title("timer")
window.geometry("380x250")
window.resizable(0,0)

label_title = tk.Label(window, text="Timer", font=("Times New Roman", 15, "bold"))
label_title.pack()

entry = tk.Entry(window, width=30, justify="center", bg="ivory", font=("Times New Roman", 15, "bold"))
entry.pack(pady=5, ipady=10)


button = tk.Button(window, text="START", font=("Times New Roman", 10, "bold"), command=start_timer, pady=10, padx=20)
button.pack(pady=10)


label = tk.Label(window, text="00:00:00", font=("DS-Digital", 50, "bold"), fg="teal")
label.pack(pady=10)

window.mainloop()

"""
Pomodoro Timer built with Tkinter
- 25 minutes work + 5 minutes break cycle
- Plays a beep sound at the start and end of each session
- Simple and clean GUI with start, pause, and reset buttons
"""

import tkinter as tk
import winsound #<-only for window system


# Default settings (in seconds)
WORK_TIME = 25 * 60   # Work duration (adjustable)
BREAK_TIME = 5 * 60   # Break duration

remaining_time = WORK_TIME
running = False
mode = "work"


# Format seconds into MM:SS
def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


# Update timer every second
def update_timer():
    global remaining_time, running, mode

    if running and remaining_time > 0:
        remaining_time -= 1
        label.config(text=format_time(remaining_time))
        root.after(1000, update_timer)

    elif running and remaining_time == 0:
        # Play beep sound when time is up
        winsound.Beep(2000, 500)

        if mode == "work":
            mode = "break"
            remaining_time = BREAK_TIME
            status_label.config(text="Break Time (5 min)")
        else:
            mode = "work"
            remaining_time = WORK_TIME
            status_label.config(text="Pomodoro Timer (25 min)")

        label.config(text=format_time(remaining_time))
        root.after(1000, update_timer)


# Start / Resume timer
def start_timer():
    global running
    # Play start beep only when beginning a fresh work session
    if remaining_time == WORK_TIME:
        winsound.Beep(2000, 500)
    if not running:
        running = True
        update_timer()


# Pause timer
def stop_timer():
    global running
    running = False


# Reset to initial state
def reset_timer():
    global remaining_time, running, mode
    running = False
    mode = "work"
    remaining_time = WORK_TIME
    status_label.config(text="Pomodoro Timer (25 min)")
    label.config(text=format_time(remaining_time))


# Main GUI window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("420x350")
root.resizable(False, False)


# Status label (shows current mode)
status_label = tk.Label(root, text="Pomodoro Timer (25 min)", font=("Arial", 14, "bold"))
status_label.pack(pady=(20, 5))


# Main time display
label = tk.Label(
    root,
    text=format_time(remaining_time),
    font=("Times New Roman", 60),
    fg="teal",
    bg="#222121",
    width=10,
    height=2
)
label.pack(pady=5)


# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=30)

tk.Button(btn_frame, text="Start", width=10, height=2, command=start_timer).pack(side="left", padx=5)
tk.Button(btn_frame, text="Reset", width=10, height=2, command=reset_timer).pack(side="left", padx=5)
tk.Button(btn_frame, text="Pause ⏸️", width=10, height=2, command=stop_timer).pack(side="left", padx=5)


root.mainloop()

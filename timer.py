import tkinter as tk

"""
A simple timer.
This window has no title bar (frameless window).
If you want to close it, please click the "exit" button.
The timer uses the "Digital-7" font.
If the font is not installed, it will fall back to the default system font.
"""


seconds = 0
running = False

# Update timer display every second
def update_timer():
    if not running:
        return
    global seconds
    seconds += 1
    mins = seconds // 60
    secs = seconds % 60
    label.config(text=f"{mins:02d}:{secs:02d}")
    root.after(1000, update_timer)


def quit_app():
    root.destroy() 

def start():
    global running
    if not running:
        running = True
        update_timer()    


def stop():
    global running
    running = False  

# Reset timer to 00:00
def reset():
    global running
    global seconds
    running = False   
    seconds = 0 
    label.config(text="00:00")
       
  

root = tk.Tk()
root.title("Timer")
root.geometry("380x200")
root.resizable(False, False)
root.overrideredirect(True)
root.config(bg="crimson")

# Timer display label
label = tk.Label(text="00:00", font=("Digital-7", 80), fg="cyan", bg="black")
label.pack(expand=True, fill="both", pady=10)

# Buttons
exit_btn = tk.Button(root, text="exit", pady=3, padx=15, command=quit_app)
exit_btn.pack(padx=5, pady=10, side="right")
reset_btn = tk.Button(root, text="reset", pady=3, padx=15, command=reset)
reset_btn.pack(padx=5, side="right")
stop_btn = tk.Button(root, text="stop", pady=3, padx=15, command=stop)
stop_btn.pack(padx=5, side="right")
start_btn = tk.Button(root, text="start", pady=3, padx=15, command=start)
start_btn.pack(padx=5, pady=10, side="right")

root.after(1000, update_timer)

root.mainloop()

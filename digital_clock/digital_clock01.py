# Digital Clock (Date, Day, Time)

import tkinter as tk
import time

# Clock update function
def clock():
    current_time = time.strftime("%H:%M:%S")   
    current_date = time.strftime("%Y.%m.%d")   
    current_day = time.strftime("%a")          
    ampm = time.strftime("%p")  # AM or PM

    label_p.config(text=ampm)
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_day.config(text=current_day)
    
    # Repeat every 1 second
    root.after(1000, clock)

# Create Tkinter window
root = tk.Tk()
root.title("Digital Clock with Date & Day")
root.config(bg="#272727")
root.geometry("390x180")
root.resizable(0,0)

time_frame = tk.Frame(root,bg="#141313", bd=2,relief="ridge")
time_frame.pack(fill="both",expand=True, padx=20,pady=20)

time_frame.grid_columnconfigure(0, weight=1) 
time_frame.grid_columnconfigure(1, weight=1) 
time_frame.grid_columnconfigure(2, weight=1)

# Date label
label_date = tk.Label(time_frame, font=("Times New Roman", 15,"bold"), bg="#141313", fg="white")
label_date.grid(row=0, column=0,sticky="nsew")

# Day label
label_day = tk.Label(time_frame, font=("Times New Roman", 15,"bold"), bg="#141313", fg="yellow")
label_day.grid(row=0, column=1,sticky="nsew")

# AM / PM label
label_p = tk.Label(time_frame, font=("Times New Roman",15, "bold"), bg="#141313", fg="#B80404")
label_p.grid(row=0, column=2,sticky="nsew")

# time label
label_time = tk.Label(time_frame, font=("Times New Roman", 60), bg="#141313", fg="cyan")
label_time.grid(row=1, column=0, columnspan=3,sticky="nsew")


# # Start clock
clock()


root.mainloop()

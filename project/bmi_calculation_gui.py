# This is a BMI calculator made using the Tkinter module.
# I made it just for fun.
# Check your health status with it.
# This code was written by a beginner, so it may not be very polished.
# If you see anything that can be improved, feel free to point it out.


# BMI calculation
import tkinter as tk
from tkinter import messagebox
import datetime

LOG_FILE = "bmi.txt"
FONT_LABEL = ("Courier", 12, "bold")


# BMI calculation function
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return bmi, status



# Function executed when the button is clicked
def on_calculate():
    try:
        name = entry_name.get().strip()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if not name:
            raise ValueError("Name is empty")

        bmi, status = calculate_bmi(height, weight)

        result_text = f"{name}'s BMI: {bmi:.1f} ({status})"
        label_result.config(text=result_text)

        # Save the result to a file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now()
            f.write(f"{timestamp} - {result_text}\n")

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric values for height and weight."
        )


# -----------------------------
# Create GUI
# -----------------------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x380")
root.config(bg="ivory")
root.resizable(False, False)

# Top spacing frame
top_space = tk.Frame(root, height=30, bg="ivory")
top_space.pack()

# Name
tk.Label(root, text="Name", font=FONT_LABEL, bg="ivory", fg="purple").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Height
tk.Label(root, text="Height (meters)", font=FONT_LABEL, bg="ivory", fg="red").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Weight
tk.Label(root, text="Weight (kg)", font=FONT_LABEL, bg="ivory", fg="teal").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

# Button
tk.Button(root, text="Calculate BMI", font=FONT_LABEL, command=on_calculate).pack(pady=10)

# Result display
label_result = tk.Label(root, text="", font=FONT_LABEL, bg="ivory", fg="navy")
label_result.pack()

root.mainloop()


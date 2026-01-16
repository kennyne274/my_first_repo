# When you run the code, a calendar is displayed in both the console and a text-based window.
# You can select this month's calendar or the full year's calendar using buttons.

import tkinter as tk
from datetime import datetime
import calendar


now = datetime.now()

YEAR = now.year
MONTH = now.month
BG = "black"
FONT = ("Arial", 12, "bold")
FG = "white"

root = tk.Tk()
root.title("Calendar")
root.geometry("680x580")
root.config(bg=BG)
root.resizable(False, False)

def date():
    cal_str = calendar.month(YEAR,MONTH)
    print(calendar.month(YEAR,MONTH))
    text.delete(1.0, tk.END)
    text.insert(tk.END, cal_str+"\n")
def year():
    print(calendar.prcal(YEAR))
    cal_year = calendar.calendar(YEAR)
    text.delete(1.0, tk.END)
    text.insert(tk.END, cal_year+"\n")
    text.insert(tk.END, "calendar has been displayed.\n")


label = tk.Label(text = "My Calendar", fg=FG, bg = BG, font=("Consolas", 12, "bold"))
label.pack(pady=(20,5))

text = tk.Text(width= 74, height= 22, fg=FG, bg=BG, font=("Consolas", 11, "bold"))
text.pack(pady=(20))

btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=10)

btn = tk.Button(btn_frame, text="This month", width = 12, height= 2, bg="aliceblue", font=FONT, command=date)
btn.grid(row=0, column=0)
btn2 = tk.Button(btn_frame, text="This year", width = 12, height= 2, bg="aliceblue", font=FONT, command=year)
btn2.grid(row=0, column=1)
root.mainloop()

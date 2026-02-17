import tkinter as tk
import random

"""
A simple program that gives you a random fortune message when you click the button.
I tried to make the messages fun and silly. Try it when you're bored!
It's a basic little app, but I hope it helps with your Python studies.
I'm still pretty new to Python myself :)
"""

# List of fortune messages
fortune_messages = [
    "Your future is bright! (Like, 3 lightbulbs bright)",
    "Good luck: You'll find an extra 1,000 won in your wallet.",
    "Everything will go smoothly today.",
    "The good news you've been waiting for is coming soon.",
    "The sky is cheering you on!",
    "Be careful today. Your boss is looking for you.",
    "There's a 99% chance you'll gain weight today.",
    "Your life-changing moment... probably in your next life!",
    "Even falling backwards, you'll still break your nose.",
    "You'll soon get a love confession... from an AI.",
    "You were born to be loved ❤️",
    "Your friend will finally pay back the money they borrowed.",
    "Everything will turn out well.",
    "Your tax bomb notice has arrived.",
    "The moment you read this, your luck begins! (Just kidding)"
]


def draw_fortune():
    """Draw a random fortune message"""
    label.config(text="Drawing your fortune...")
    label.update()
    root.after(800, lambda: label.config(text=random.choice(fortune_messages)))


root = tk.Tk()
root.title("Today's Fortune Slip 💌")
root.resizable(False, False)

# Background image (fallback to ivory color if file is missing)
try:
    bg_image = tk.PhotoImage(file="field.png")
    canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
    canvas.pack()
    canvas.create_image(400, 300, image=bg_image)
except Exception as e:
    print("Could not find the image file.", e)
    canvas = tk.Canvas(root, width=800, height=600, bg="ivory", highlightthickness=0)
    canvas.pack()


label = tk.Label(
    root,
    text="Click the button to draw today's fortune!",
    font=("Arial", 24, "bold"),  # Change font if you prefer something else
    fg="#3e2723",
    bg="#ffecb3",
    wraplength=600,
    pady=20
)
label.place(x=400, y=180, anchor="center")


button = tk.Button(
    root,
    text="Draw Fortune 🎲",
    font=("Arial", 28, "bold"), 
    command=draw_fortune,
    bg="#a7ffeb",
    fg="#00695c",
    activebackground="#64ffda",
    relief="raised",
    bd=8,
    padx=20,
    pady=10,
    cursor="hand2"
)
button.place(x=400, y=350, anchor="center")

root.mainloop()

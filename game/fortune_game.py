import tkinter as tk
import random

"""
A simple program that gives you a random fortune message when you click the button.
I tried to make the messages fun and silly. Try it when you're bored!
It's a basic little app, but I hope it helps with your Python studies. :)

"""

# List of fortune messages
fortune_messages = [
    "Your future is so bright... you'll need sunglasses (and therapy).",
    "Good luck: You'll find an extra $100 in your pocket.",
    "Today will be smooth... like your dating life. (Spoiler: not at all.)",
    "The good news is coming. Probably next Tuesday.",
    "The universe is rooting for you.",
    "Watch out today. Your boss is about to 'have a quick chat' with you.",
    "99% chance you'll gain weight today.",
    "Your big break is coming...",
    "Even when life knocks you down, you'll land face-first. Classic you.",
    "A love confession is on its way... probably from your AI chatbot.",
    "You were born to be loved!",
    "Your friend will pay you back!",
    "Everything's going to be okay!",
    "Your tax refund has arrived. Psych! It's a bill for $500 more.",
    "Luck starts the second you read this... said every scammy cookie ever. (Just kidding... or am I?)"
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
    bg_image = tk.PhotoImage(file=r"C:\Users\user\Desktop\python\field.png")
    canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
    canvas.pack()
    canvas.create_image(400, 300, image=bg_image)
except Exception as e:
    print("Could not find the image file.", e)
    canvas = tk.Canvas(root, width=800, height=600, bg="ivory", highlightthickness=0)
    canvas.pack()

# Title label
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

# Fortune draw button
button = tk.Button(
    root,
    text="Draw Fortune 🎲",
    font=("Arial", 28, "bold"),  # Keep Korean font or change to "Arial" etc.
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

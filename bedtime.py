import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen

def draw_moon():
    moon = [
        "   🌙   ",
        "  🌙🌙  ",
        " 🌙🌙🌙 ",
        "🌙🌙🌙🌙",
        " 🌙🌙🌙 ",
        "  🌙🌙  ",
        "   🌙   "
    ]
    for line in moon:
        print(line.center(40))
        time.sleep(0.5)

print("Hey... it's late. I'm getting sleepy too.")
print("Let me count down for you...\n")

for i in range(5, 0, -1):
    clear()
    print(f"Bedtime in... {i}")
    time.sleep(0.7)
    draw_moon()
    time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
print("   Zzz...   ")
print("Goodnight. See you when you're rested.")

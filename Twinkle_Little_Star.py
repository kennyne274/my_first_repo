# stars appear one by one on a black night sky while playing "Twinkle Twinkle Little Star" 
# I think  sometimes I am really bored.

import turtle
import random
import time
import sys
import winsound  # Windows only


#   Twinkle Twinkle Little Star melody (frequency, milliseconds)

# C4=262, D4=294, E4=330, F4=349, G4=392, A4=440, etc.
melody = [
    (262, 400), (262, 400), (392, 400), (392, 400),
    (440, 400), (440, 400), (392, 800),
    (349, 400), (349, 400), (330, 400), (330, 400),
    (294, 400), (294, 400), (262, 800),
    
    (392, 400), (392, 400), (349, 400), (349, 400),
    (330, 400), (330, 400), (294, 800),
    (392, 400), (392, 400), (349, 400), (349, 400),
    (330, 400), (330, 400), (294, 800),
    
    (262, 400), (262, 400), (392, 400), (392, 400),
    (440, 400), (440, 400), (392, 800),
    (349, 400), (349, 400), (330, 400), (330, 400),
    (294, 400), (294, 400), (262, 800),
]

def play_twinkle():
    """Play Twinkle Twinkle Little Star melody in a loop"""
    while True:
        for freq, duration in melody:
            try:
                winsound.Beep(freq, duration)
                time.sleep(0.03)  # Slight pause between notes
            except:
                # Skip if winsound is unavailable or interrupted
                pass
        time.sleep(1.5)  # Short pause after each full play 



# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.title("Starry Night with Twinkle Twinkle Little Star♪")
screen.tracer(0)


# Star drawing function
def draw_star(x, y, size=20):

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#FFFF99")  # Light yellow star
    t.begin_fill()
    t.pensize(2)
    
    for _ in range(5):
        t.forward(size)
        t.right(144)
    
    t.end_fill()
    t.penup()


# ────────────────
print("A new star appears every second... (total 30 stars)")
print("Twinkle Twinkle Little Star melody is playing (Windows only)")

import threading
music_thread = threading.Thread(target=play_twinkle, daemon=True)
music_thread.start()

stars_drawn = 0
total_stars = 30

while stars_drawn < total_stars:
    try:
        x = random.randint(-420, 420)
        y = random.randint(-320, 320)
        
        draw_star(x, y, size=20)
        
        screen.update()
        
        stars_drawn += 1
        time.sleep(1)  # Wait 1 second
        
    except KeyboardInterrupt:
        print("\nUser terminated the program.")
        sys.exit() 
    except Exception as e:
        print("Loop interrupted")
        sys.exit() 

print("All stars created! (Total: 30)")
print("Close the window or press Ctrl+C to exit.")


screen.mainloop()

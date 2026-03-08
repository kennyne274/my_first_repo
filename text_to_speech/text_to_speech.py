import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from playsound3 import playsound
from gtts import gTTS
import threading
import uuid
import os

# Text-to-Speech program that reads input text aloud
# Requires gTTS and playsound3 libraries to run
# pip install gTTS
# pip install playsound3

# Creates a gTTS object to convert text to speech
def generate_tts(text):
    # Get language code from the combobox selection
    lang = languages[input_lang.get()]
    speed = speed_menu.get()

    if speed == "slow":
        slow = True
    else:
        slow = False

    # Create gTTS object (text → speech data)
    try:
        tts = gTTS(text,
                    lang=lang,
                    slow=slow)
        return tts
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during playback\n{e}")
        return

# Generates speech and plays it (runs in a separate thread)
def play(text):
    tts = generate_tts(text)

    # Prevent filename conflicts
    filename = f"{uuid.uuid4()}.mp3"
    tts.save(filename)
    playsound(filename)
    # Delete the played file
    try:
        os.remove(filename)
    except PermissionError:
        pass

    root.after(0, lambda: speak_btn.config(state="normal"))

# Gets the input text and triggers speech playback
def speak_text():
    text = text_area.get("1.0", tk.END).strip()

    # Show warning if input is empty
    if not text:
        messagebox.showwarning("Input Error", "Please enter a sentence")
        return

    speak_btn.config(state="disabled")

    # Run speech generation and playback in a background thread
    # Prevents GUI from freezing
    thread = threading.Thread(target=play, args=(text,), daemon=True)
    thread.start()

# Saves the speech data as an MP3 file
def save_audio():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter a sentence")
        return

    # Choose save location and filename
    file = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")]
    )

    if not file:
        return

    tts = generate_tts(text)
    if not tts:
        root.after(0, lambda: speak_btn.config(state="normal"))
        return

    tts.save(file)

# Language list
languages = {  
    "Korean": "ko",
    "English": "en",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Japanese": "ja",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Italian": "it",
    "Russian": "ru",
    "Thai": "th",
    "Polish": "pl",
    "Hebrew": "he",
    "Vietnamese": "vi",
    "Hindi": "hi"
}

# ================== GUI ================== #

root = tk.Tk()
root.title("text to speech converter")
root.geometry("600x480")
root.resizable(0, 0)

# Title
title_label = ttk.Label(root, text="Text-to-Speech program", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# text_frame
text_frame = tk.Frame(root)
text_frame.pack()

# scrollbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

# text_area
text_area = tk.Text(text_frame, height=14, width=80, font=("Arial", 12, "bold"))
text_area.pack(side="left")
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Frame for options
options_frame = ttk.Frame(root)
options_frame.pack(pady=10)

# Speech playback speed
ttk.Label(options_frame, text="Speed :").grid(row=0, column=0)
speed_var = tk.StringVar(value="fast")
speed_menu = ttk.Combobox(options_frame, textvariable=speed_var, values=["fast", "slow"], width=15, state="readonly")
speed_menu.grid(row=0, column=1, pady=10, padx=10)

ttk.Label(options_frame, text="Input Language").grid(row=0, column=2, pady=10, padx=10)

# Language selection combobox
input_lang = ttk.Combobox(options_frame, values=list(languages.keys()), state="readonly", width=15)
input_lang.grid(row=0, column=3, pady=10, padx=10)
input_lang.set("English")

# Button frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

# Speak button
speak_btn = tk.Button(button_frame, text="Speak",
                      command=speak_text,
                      width=10,
                      height=1,
                      font=("Times New Roman", 15, "bold"),
                      bg="#049F95",
                      fg="white")
speak_btn.grid(row=0, column=2, padx=10)

# Save button
save_btn = tk.Button(button_frame,
                     text="Save",
                     command=save_audio,
                     width=10,
                     height=1,
                     font=("Times New Roman", 15, "bold"),
                     bg="#1BA0F3",
                     fg="white")
save_btn.grid(row=0, column=3, padx=10)

root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Use Google Translator from deep-translator
# Install with: pip install deep-translator
from deep_translator import GoogleTranslator


def translate():
    """Translate the input text to the selected target language."""
    try:
        input_str = input_text.get("1.0", "end").strip()
        
        # Show warning if input is empty
        if not input_str:
            messagebox.showwarning("Warning", "Please enter some text!")
            return
        
        # Get selected language codes
        source_lang = languages[input_lang.get()]
        target_lang = languages[output_lang.get()]
        
        # Show info if source and target languages are the same
        if source_lang == target_lang:
            messagebox.showinfo("Info", "Source and target languages are the same!")
            return
        
        # Perform translation
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(input_str)
        
        # Display result
        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated)

    except KeyboardInterrupt:
        messagebox.showwarning("Error", "Program terminated.")
    except ConnectionError:
        messagebox.showerror("Error", "Please check your internet connection.")
    except Exception as e:
        messagebox.showwarning("Error", "An unknown error occurred.")


def delete():
    """Clear both input and output text areas."""
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("Multi-Language Translator")
root.geometry("620x630")
root.resizable(False, False)


# Supported languages (display name: language code)
languages = {
    "Auto Detect": "auto",
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

# Output language options (no "Auto Detect")
languages2 = {
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


tk.Label(root, text="Input Language").place(x=30, y=20)

# Input language combobox
input_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly", width=22)
input_lang.place(x=130, y=20)
input_lang.set("Auto Detect")

tk.Label(root, text="Output Language").place(x=30, y=60)

# Output language combobox
output_lang = ttk.Combobox(root, values=list(languages2.keys()), state="readonly", width=22)
output_lang.place(x=130, y=60)
output_lang.set("Korean")

tk.Label(root, text="Text to Translate").place(x=30, y=110)

# Input text area with scrollbar
input_frame = tk.Frame(root)
input_frame.place(x=30, y=140)

input_text = tk.Text(
    input_frame,
    width=69,
    height=9,
    font=("Arial", 11)   
)
input_text.pack(side="left")

input_scroll = tk.Scrollbar(input_frame)
input_scroll.pack(side="right", fill="y")

input_text.config(yscrollcommand=input_scroll.set)
input_scroll.config(command=input_text.yview)

tk.Label(root, text="Translation Result").place(x=30, y=340)

# Output text area with scrollbar
output_frame = tk.Frame(root)
output_frame.place(x=30, y=370)

output_text = tk.Text(
    output_frame,
    width=69,
    height=9,
    font=("Malgun Gothic", 11),
    wrap="word"
)
output_text.pack(side="left")

output_scroll = tk.Scrollbar(output_frame)
output_scroll.pack(side="right", fill="y")

output_text.config(yscrollcommand=output_scroll.set)
output_scroll.config(command=output_text.yview)


# Buttons
btn1 = tk.Button(root, text="Translate", width=10, height=1, command=translate)
btn1.place(x=220, y=575)

btn2 = tk.Button(root, text="Reset", width=10, height=1, command=delete)
btn2.place(x=320, y=575)


root.mainloop()

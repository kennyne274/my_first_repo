from tkinter import *
from tkinter import filedialog
import os
import shutil


# File categories by extension
file_folder = {
    ".jpg": "Images", ".jpeg": "Images", 
    ".png": "Images", ".gif": "Images",

    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos",

    ".mp3": "Audio", ".wav": "Audio", 

    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents", 
    ".txt": "Documents", ".csv": "Documents", ".hwp": "Documents",

    ".py": "Code", ".js": "Code", ".html": "Code",
    ".css": "Code", ".c": "Code",

    ".zip": "Archives", ".rar": "Archives",
    ".tar": "Archives", ".gz": "Archives",

    ".exe": "Installers", 
}


# Select folder
def select_folder():
    global selected_folder

    path = filedialog.askdirectory()
    folder_entry.delete(0, END)
    folder_entry.insert(0, path)
    selected_folder = path


# Organize files + extension statistics
def organize_files():

    source_dir = selected_folder
    dest_dir = selected_folder

    if not source_dir:
        result_text.insert(END, "Please select a folder first.\n")
        return

    ext_count = {}      # Count per extension
    total_files = 0     # Total files processed

    for file in os.listdir(source_dir):

        if file.startswith("."):
            continue

        filepath = os.path.join(source_dir, file)

        if not os.path.isfile(filepath):
            continue

        total_files += 1

        # Get extension
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext not in ext_count:
            ext_count[ext] = 0

        ext_count[ext] += 1

        # Find destination folder
        folder = file_folder.get(ext, "Other")

        dest = os.path.join(dest_dir, folder)
        os.makedirs(dest, exist_ok=True)

        target_path = os.path.join(dest, file)

        counter = 1

        # Handle duplicate filenames
        while os.path.exists(target_path):
            new_name = f"{name} ({counter}){ext}"
            target_path = os.path.join(dest, new_name)
            counter += 1

        try:
            shutil.move(filepath, target_path)

        except PermissionError:
            print(f"Permission denied: {file}")

        except Exception as e:
            print(f"Error moving {file}: {e}")

    # Show result
    result_text.delete(1.0, END)

    result_text.insert(END, f"📂 Total files processed: {total_files}\n\n")
    result_text.insert(END, "File type statistics\n\n")

    for ext, count in ext_count.items():
        result_text.insert(END, f"{ext} : {count} files\n")

    result_text.insert(END, "\nFile organization completed.")


# GUI 
window = Tk()
window.title("File Organizer")
window.geometry("650x450")

selected_folder = ""

# Title label
label_title = Label(window, text="File Organizer", font=("Arial", 18, "bold"))
label_title.pack(pady=(20, 10))

frame = LabelFrame(window, text="Select Folder", height=7)
frame.pack(fill="both", padx=20, pady=5)

# Select folder button
Button(frame,
       text="Select Folder",
       command=select_folder,
       width=20, height=2).pack(padx=20, pady=20, side="right")


# Display selected directory path
folder_entry = Entry(frame, width=55)
folder_entry.insert(0, "No folder selected")
folder_entry.pack(padx=20, pady=10, side="left", ipady=5)

frame_start = LabelFrame(window, text="Organize Files", height=7)
frame_start.pack(fill="both", padx=20, pady=5)

# Start button
Button(frame_start,
       text="Start Organizing",
       command=organize_files,
       width=20, height=2).pack(padx=20, pady=20, side="right")


# Result display area
result_text = Text(frame_start, height=15)
result_text.pack(side="left", padx=20, pady=10)

window.mainloop()


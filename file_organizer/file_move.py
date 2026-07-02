import os
import shutil

"""This program filters .py and .ipynb files and moves them to the specified folder."""

# File moving function (parent path, source folder, target folder)
def file_move(parent_path, source_folder, target_folder):

   # Create the paths for the source and target folders.
    source_path = os.path.join(parent_path, source_folder)   
    target_path = os.path.join(parent_path, target_folder) 

    os.makedirs(target_path, exist_ok=True) 

    try:    
        for file in os.listdir(source_path):
            file_path = os.path.join(source_path, file)
           
            if os.path.isdir(file_path):
                continue 
            # Move files with the '.py' or '.ipynb' extension to the target folder.
            if file.lower().endswith((".py", ".ipynb")): 
                try: 
                    shutil.move(file_path, target_path)
                except PermissionError:
                    print(f"Permission denied: {file}")
                except shutil.Error:
                    print(f"Failed to move file: {file}")

    except FileNotFoundError:
        print("The specified path could not be found.")


if __name__ == "__main__":

    home = os.path.expanduser("~") 
    desktop = os.path.join(home, "Desktop") 

    file_move(desktop, "files", "my_file")
    print(os.listdir(os.path.join(desktop, "my_file")))

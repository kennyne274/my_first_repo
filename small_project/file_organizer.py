

import os


# Determine file category based on extension
def categorize_file(filename):
    filename = filename.lower()
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        return "images"
    elif filename.endswith(('.txt', '.pdf', '.docx', '.log')):
        return "texts"
    else:
        return "others"


# Create folders if needed and move files into categories
def organize_directory(path):
    # 1. Define and create target folders
    categories = ["images", "texts", "others"]
    for category in categories:
        target_dir = os.path.join(path, category)
        os.makedirs(target_dir, exist_ok=True)

    # 2. Iterate through items and move files
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        # Skip directories
        if os.path.isdir(full_path):
            continue

        category = categorize_file(item)
        destination = os.path.join(path, category, item)

        try:
            os.rename(full_path, destination)
            print(f"[Moved] {item} → {category}/")
        except OSError as e:
            print(f"[Error] Failed to move {item}: {e}")


def main(directory_path):
    try:
        organize_directory(directory_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()


if __name__ == "__main__":
    user_input = input("Enter the folder path to organize: ").strip()

    if not os.path.exists(user_input):
        print("The specified path does not exist. Exiting.")
    else:
        main(user_input)


        print("\nOrganization complete!")

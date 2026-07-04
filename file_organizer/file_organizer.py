import shutil
from pathlib import Path

def get_downloads_folder():
    home = Path.home()
    downloads = home / "Downloads" 
    if downloads.exists():
        return downloads
    else:
        raise FileNotFoundError("Download folder not found.")

def organize_files(src): 

    moved = 0 
    skipped_count = 0 

    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'Documents': ['.csv','.pdf', '.doc', '.docx', '.xls','.txt', '.xlsx', '.ppt', '.pptx', '.hwpx'],
        'Code' : ['.py', '.ipynb', '.c', '.html', '.css', '.js'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Installers': ['.exe', '.msi', '.dmg', '.apk']
    }

    source = src
    
    for category, exts in categories.items():
        folder = source / category
        folder.mkdir(exist_ok=True)

    for file in source.iterdir():  
        if not file.is_file():
            continue

        for category, exts in categories.items():
            if file.suffix.lower() in exts:                    
                dest = source / category / file.name 
                if not dest.exists():
                    try:
                        shutil.move(file, dest)
                        print(f"{category}: {file.name}")
                        moved += 1
                    except shutil.Error:
                        print(f"Failed to move files {file.name}")
                        skipped_count += 1
                    except PermissionError:
                        print(f"PermissionError: {file.name}")
                        skipped_count += 1

       
                else:               
                    counter = 1
                    original_name = dest.stem
                    ext = dest.suffix
                    while True:
                        new_file = source / category / f"{original_name} ({counter}){ext}"
                        if not new_file.exists():
                            try:
                                shutil.move(file, new_file)                               
                                print(f"{category}: {new_file.name}")
                                moved += 1
                            except Exception:
                                print(f""Failed to move files {file.name}")
                                skipped_count += 1
                                
                            break

                        counter += 1
            
                break
        
      
        else:  
            other = source / "others"
            other.mkdir(exist_ok=True)
            try:
                shutil.move(file, other / file.name)
                print(f"Other: {file.name}")
                moved += 1
            except Exception:
                print(f""Failed to move files {file.name}")
                skipped_count += 1

    print(f"\n{moved} file moves complete.")

if __name__ == "__main__":
    src = get_downloads_folder()
    organize_files(src)

from pathlib import Path
from collections import Counter
import os
from collections import Counter

# กำหนด category ตามนามสกุล
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".avi", ".mkv", ".mov"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".go"],
}

def get_category(file_extension):
    result="Others"
    #print("file_extension : ",file_extension)
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            #print(f"category is : {category}")
            result=category
            break
    return result
    


def scan_files(directory):
    files_return=[]
    for f in directory.iterdir() :
        if f.is_file():
            files_return.append({
                "name":f.name,
                "category":get_category(f.suffix),
                "size":f.stat().st_size
            })
    return files_return


def organize_files(directory, dry_run=True):
    path = Path(directory)
    files = scan_files(directory)
    moved_count = 0
    if dry_run:
        print("\n===== Dry Run =====")
    else:
        print("\n===== Organize Files =====")
    for f in files:
        category_folder = path / f["category"]
        source = path / f["name"]
        destination = category_folder / f["name"]
        if dry_run:
            print(f"Would move: {f['name']} → {f['category']}/")
        else:
            category_folder.mkdir(exist_ok=True)
            source.rename(destination)
            print(f"Moved: {f['name']} → {f['category']}/")
            moved_count += 1
    if not dry_run:
        print(f"\nDone! Organized {moved_count} files.")
      
    return

def show_summary(directory):
    files=scan_files(directory)
    return Counter([f["category"] for f in files])

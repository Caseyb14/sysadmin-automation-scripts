import os
import shutil

# Define the directory to organize (usually your Downloads folder)
# Users would change this path to their own
source_dir = "C:\\Users\\Public\\Downloads"

# Define the categories and their extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Installers": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z"]
}

def organize_files():
    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories, only move files
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to correct folder
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if file_ext in extensions:
                # Create category folder if it doesn't exist
                category_path = os.path.join(source_dir, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                # Move the file
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved {filename} to {category}")
                moved = True
                break
        
        # Optional: Move everything else to a "Misc" folder
        if not moved:
            misc_path = os.path.join(source_dir, "Misc")
            if not os.path.exists(misc_path):
                os.makedirs(misc_path)
            shutil.move(file_path, os.path.join(misc_path, filename))
            print(f"Moved {filename} to Misc")

if __name__ == "__main__":
    organize_files()

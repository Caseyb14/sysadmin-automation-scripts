# SysAdmin Automation Tools

A collection of Python scripts designed to automate repetitive administrative tasks and improve workflow efficiency.

## Tools Included

### 1. Automated Downloads Organizer (`file_organizer.py`)
* **Problem:** The Downloads folder quickly becomes cluttered with mixed file types (PDFs, Installers, Images), making it difficult to find critical documents.
* **Solution:** This Python script scans the target directory and automatically sorts files into sub-folders based on extension.
* **Tech Used:** Python `os` and `shutil` libraries for file manipulation.

## How to Run
1. Update the `source_dir` variable in the script to match your target folder.
2. Run via terminal: `python file_organizer.py`

# SysAdmin Automation Suite

A collection of Python scripts designed to automate core administrative tasks: file management, infrastructure monitoring, and security auditing.

## Tools Included

### 1. Automated Downloads Organizer (`file_organizer.py`)
* **Problem:** Downloads folders often become chaotic dumping grounds, wasting time when retrieving documents.
* **Solution:** Scans a directory and automatically sorts files into sub-folders based on extension (PDFs, Images, Installers).
* **Tech Used:** `shutil`, `os` modules.

### 2. Disk Health Monitor (`disk_monitor.py`)
* **Problem:** Servers can crash unexpectedly if log files consume all available disk space.
* **Solution:** Checks the system's disk usage and triggers an alert if free space falls below a critical threshold (e.g., 20%). Designed to be run as a cron job.
* **Tech Used:** `shutil.disk_usage`.

### 3. Security Log Parser (`log_analyzer.py`)
* **Problem:** Manually reviewing server logs for intrusion attempts is impossible at scale.
* **Solution:** scans text-based log files for specific threat indicators (keywords like "Failed", "Unauthorized") and extracts the exact line number for review.
* **Tech Used:** String parsing, File I/O.

## How to Run
1. **Organizer:** Update `source_dir` in the script and run `python file_organizer.py`
2. **Monitor:** Run `python disk_monitor.py` (Exit code 1 indicates low space).
3. **Analyzer:** Ensure a log file exists and run `python log_analyzer.py`

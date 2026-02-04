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

### 4. Lab Environment Launcher (`lab_launcher.py`)
* **Problem:** Setting up the home lab requires manually launching 3 separate Virtual Machines (Splunk, Windows, Kali), which is tedious.
* **Solution:** A Python automation script that interfaces with the VirtualBox Hypervisor (`VBoxManage`). It sequentially boots the machines with a safety delay to prevent host CPU spikes.
* **Tech Used:** `subprocess` module, Hypervisor CLI automation.

### 5. Automated Traffic Generator (`traffic_generator.py`)
* **Problem:** Home labs are often silent, making it hard to test SIEM alerts or practice threat hunting without manually launching attacks.
* **Solution:** A "Purple Team" script that runs on a Kali Linux node. It randomizes network probes (Nmap scans, ICMP pings, and simulated Brute Force attempts) against a target VM at irregular intervals to generate realistic noise in Splunk/Sysmon logs.
* **Tech Used:** Python `subprocess`, `random`, and standard Linux security tools (`nmap`, `hydra`).
* **Note:** For educational/lab use only.

### 6. Ransomware Simulator (`ransom_simulator.py`)
* **Problem:** Detecting ransomware behavior (mass file modification) requires realistic test data, but running real malware is too dangerous.
* **Solution:** A safe simulation script that creates a sandbox directory (`./simulation_data`), populates it with dummy files, and performs a "reversible encryption" (text reversal) and file renaming action.
* **Goal:** Triggers "File Creation", "File Deletion", and "Extension Change" events in Sysmon/Splunk for rule testing.
* **Safety:** Strictly limited to its own sub-folder; does not touch system files.

## How to Run
1. **Organizer:** Update `source_dir` in the script and run `python file_organizer.py`
2. **Monitor:** Run `python disk_monitor.py` (Exit code 1 indicates low space).
3. **Analyzer:** Ensure a log file exists and run `python log_analyzer.py`
4. **Launcher:** Update the `VMS_TO_START` list inside the script with your specific VM names, then run `python lab_launcher.py`
5. **Generator:** Update `VICTIM_IP` to your target's address and run `python traffic_generator.py` (Press CTRL+C to stop the simulation).
6. **Ransom Sim:** Run `python ransom_simulator.py` (It will create a folder, encrypt the dummy files inside, and drop a note).

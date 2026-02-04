import shutil
import sys

# Configuration: Set the threshold (e.g., 20% free space required)
MIN_FREE_PERCENT = 20
# Directory to check (root by default)
CHECK_DIR = "/"

def check_disk_usage(directory):
    total, used, free = shutil.disk_usage(directory)
    
    # Calculate percentages
    total_gb = total / (2**30)
    free_gb = free / (2**30)
    percent_free = (free / total) * 100
    
    print(f"--- Disk Usage Report for {directory} ---")
    print(f"Total: {total_gb:.2f} GB")
    print(f"Free:  {free_gb:.2f} GB ({percent_free:.2f}%)")
    
    # Alert Logic
    if percent_free < MIN_FREE_PERCENT:
        print(f"[!] ALERT: Free space is critically low (Under {MIN_FREE_PERCENT}%)!")
        return False
    else:
        print("[+] Status: Healthy")
        return True

if __name__ == "__main__":
    # If the check fails (returns False), exit with an error code
    if not check_disk_usage(CHECK_DIR):
        sys.exit(1)

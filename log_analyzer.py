import os

# Configuration
LOG_FILE = "server_logs.txt"  # You would point this to /var/log/auth.log in real life
KEYWORDS = ["error", "failed", "unauthorized", "critical"]

def analyze_log(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    print(f"--- Scanning {file_path} for threats ---")
    found_issues = 0
    
    with open(file_path, 'r') as f:
        # Enumerate gives us the line number (i) and the content (line)
        for i, line in enumerate(f, 1):
            # Check for each keyword (case-insensitive)
            for key in KEYWORDS:
                if key in line.lower():
                    print(f"[Line {i}] ALERT Found '{key}': {line.strip()}")
                    found_issues += 1
    
    if found_issues == 0:
        print("[+] No suspicious activity found.")
    else:
        print(f"\n[!] Scan Complete: {found_issues} potential issues detected.")

if __name__ == "__main__":
    # Create a dummy log file for testing if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("2025-01-01 10:00:00 INFO System started\n")
            f.write("2025-01-01 10:05:00 WARNING Failed login attempt from 192.168.1.5\n")
            f.write("2025-01-01 10:10:00 INFO User logged in\n")
    
    analyze_log(LOG_FILE)

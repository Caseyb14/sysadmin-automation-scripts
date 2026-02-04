import subprocess
import time
import sys

# CONFIGURATION
# Replace these with your EXACT VirtualBox VM names
# You can find them by running: VBoxManage list vms
VMS_TO_START = [
    "Splunk-SIEM",      # Your Blue Team Box
    "Windows-Victim",   # Your Target
    "Kali-Attacker"     # Your Red Team Box
]

# Path to VBoxManage (Standard on Windows)
VBOX_MANAGE_PATH = r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"

def start_vm(vm_name):
    print(f"[...] Attempting to start {vm_name}...")
    try:
        # --type headless starts it in background (good for servers/Splunk)
        # --type gui starts it with a window (good for Kali/Desktop)
        mode = "headless" if "Splunk" in vm_name else "gui"
        
        subprocess.run([VBOX_MANAGE_PATH, "startvm", vm_name, "--type", mode], check=True)
        print(f"[+] {vm_name} started successfully in {mode} mode.")
        return True
    except subprocess.CalledProcessError:
        print(f"[!] Error: Could not start {vm_name}. It might be running already.")
        return False
    except FileNotFoundError:
        print(f"[!] Critical: VBoxManage not found at {VBOX_MANAGE_PATH}")
        sys.exit(1)

def main():
    print("--- 🚀 Initializing Cyber Range Sequence ---")
    
    for vm in VMS_TO_START:
        start_vm(vm)
        # Wait 10 seconds between starts to avoid freezing your PC (CPU spike protection)
        print("    Waiting 10s for stability...")
        time.sleep(10)
        
    print("\n[+] Lab Environment is ONLINE.")

if __name__ == "__main__":
    main()

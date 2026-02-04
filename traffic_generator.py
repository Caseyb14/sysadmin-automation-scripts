import subprocess
import time
import random
import sys

# CONFIGURATION
# IP Address of your Windows Victim VM
VICTIM_IP = "192.168.56.102"  # CHANGE THIS to your actual Victim IP

def run_nmap_scan():
    print(f"[!] Launching Port Scan on {VICTIM_IP}...")
    # Runs a fast scan (-F) without ping (-Pn) to ensure logs are generated
    try:
        subprocess.run(["nmap", "-F", "-Pn", VICTIM_IP], stdout=subprocess.DEVNULL)
        print("[+] Scan Complete.")
    except FileNotFoundError:
        print("[Error] Nmap not installed. Skipping.")

def run_hydra_simulation():
    print(f"[!] Simulating SMB Brute Force on {VICTIM_IP}...")
    # We don't need real Hydra; we just need to generate "Event 4625" (Failed Login)
    # We try to mount the C$ share with a bad password 5 times
    for i in range(3):
        subprocess.run(
            ["hydra", "-l", "admin", "-p", "badpass", "smb://" + VICTIM_IP],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    print("[+] Brute Force Simulation Complete.")

def run_ping_sweep():
    print(f"[!] Pinging {VICTIM_IP} to test connectivity...")
    # Standard ping to generate ICMP traffic
    subprocess.run(["ping", "-c", "4", VICTIM_IP], stdout=subprocess.DEVNULL)
    print("[+] Ping Sweep Complete.")

def main():
    print("--- ⚔️ Automated Red Team Traffic Generator ⚔️ ---")
    print(f"Targeting: {VICTIM_IP}")
    print("Press CTRL+C to stop.")

    actions = [run_nmap_scan, run_hydra_simulation, run_ping_sweep]

    while True:
        # 1. Select a random attack
        action = random.choice(actions)
        
        # 2. Execute it
        action()
        
        # 3. Wait for a random time (e.g., between 30 seconds and 5 minutes)
        # This makes it "unpredictable" for the Blue Team (You)
        sleep_time = random.randint(30, 300) 
        print(f"--- Sleeping for {sleep_time} seconds ---\n")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

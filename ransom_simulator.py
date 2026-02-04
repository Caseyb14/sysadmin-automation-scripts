import os
import time
import sys

# CONFIGURATION
# The folder to attack (We create this automatically to be safe)
TARGET_DIR = "simulation_data"
# The extension to append (e.g., .encrypted)
ENC_EXT = ".locked"

def setup_simulation():
    """Creates a dummy folder with dummy files to 'infect'."""
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"[+] Created sandbox directory: {TARGET_DIR}")
    
    # Create 10 dummy files
    for i in range(1, 11):
        with open(f"{TARGET_DIR}/critical_file_{i}.txt", "w") as f:
            f.write(f"This is meaningful data {i}" * 100)
    print(f"[+] Populated {TARGET_DIR} with 10 dummy files.")

def simulate_encryption():
    """The 'Attack': Renames files and scrambles content."""
    print(f"[!] STARTING ENCRYPTION SIMULATION ON {TARGET_DIR}...")
    
    files = [f for f in os.listdir(TARGET_DIR) if not f.endswith(ENC_EXT)]
    
    if not files:
        print("[*] No target files found. Run setup first?")
        return

    for filename in files:
        file_path = os.path.join(TARGET_DIR, filename)
        
        # 1. Read the original data
        with open(file_path, "r") as f:
            data = f.read()
        
        # 2. 'Encrypt' it (Simple Reversal for safety)
        encrypted_data = data[::-1]
        
        # 3. Write new file
        new_name = file_path + ENC_EXT
        with open(new_name, "w") as f:
            f.write(encrypted_data)
            
        # 4. Delete original (The noisy part)
        os.remove(file_path)
        print(f"[>] Encrypted: {filename} -> {filename}{ENC_EXT}")
        time.sleep(0.5) # Slow down slightly so we can see it happening

def drop_ransom_note():
    """Drops the scary text file."""
    note_path = os.path.join(TARGET_DIR, "READ_ME_NOW.txt")
    with open(note_path, "w") as f:
        f.write("YOUR FILES HAVE BEEN ENCRYPTED (SIMULATION).\n")
        f.write("This is a benign test for SIEM detection.\n")
    print(f"[!] Ransom note dropped: {note_path}")

if __name__ == "__main__":
    print("--- ☣️ Ransomware Detection Test ☣️ ---")
    print("WARN: This will modify files in the './simulation_data' folder.")
    
    # Step 1: Create the playground
    setup_simulation()
    time.sleep(2)
    
    # Step 2: Run the 'attack'
    simulate_encryption()
    
    # Step 3: Leave the note
    drop_ransom_note()
    
    print("\n[+] Simulation Complete. Check your Splunk for 'File Create' and 'File Delete' events.")

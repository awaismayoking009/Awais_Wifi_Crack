import os
import time
import subprocess
from colorama import Fore, Style, init

# Initialize colorama for Windows/Linux compatibility
init()

# Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE

def banner():
    os.system('clear')
    print(f"""
{R}  _____  _      _____  _           _   _             _    
 |  __ \(_)    / ____|(_)         | | | |           | |   
 | |__) |_ ___| |  __  _ _ __ ___| |_| |__   __ _  | | __
 |  ___/| / __| | |_ || | '__/ _ \ __| '_ \ / _` | | |/ /
 | |    | \__ \ |__| || | | |  __/ |_| | | | (_| | |   < 
 |_|    |_|___/\_____||_|_|  \___|\__|_| |_|\__,_| |_|\_\
                                                          
      {W}☠️  {R}Wifi Attack Awais Mayo  {W}💀
      {B}💀  {C}Powered By Awais Mayo   {B}👑
    """)

def scan_wifi():
    print(f"\n{C}[*] Scanning for Networks (BSSID, Channel, Encryption)...{W}")
    # Simulation of a professional scan
    time.sleep(2)
    print(f"{G}ID   BSSID              CH   RSSI   ESSID{W}")
    print(f"{W}01   00:11:22:33:44:55  06   -45    Home_WiFi_5G")
    print(f"02   AA:BB:CC:DD:EE:FF  11   -60    Office_Net")
    print(f"\n{Y}[!] Select a target ID to proceed.{W}")

def capture_handshake():
    target = input(f"\n{C}Enter Target BSSID > {W}")
    print(f"{R}[!] Starting Deauthentication Attack on {target}...{W}")
    # 
    time.sleep(3)
    print(f"{G}[+] WPA Handshake Captured! File saved as 'handshake.cap'{W}")

def bypass_crack():
    print(f"\n{Y}[*] Loading Advanced Wordlist and Brute-force Engine...{W}")
    time.sleep(2)
    # 
    for i in range(1, 4):
        print(f"{R}[-] Testing passwords: {i*5000} per second...{W}")
        time.sleep(1)
    print(f"\n{G}[✔] CRACK SUCCESSFUL!{W}")
    print(f"{C}PASSWORD FOUND: {W}AwaisMayo@786")

def main():
    while True:
        banner()
        print(f"{G}[1]{W} Scan Nearby Wi-Fi (Technical Details) 📡")
        print(f"{G}[2]{W} Capture WPA Handshake (Advanced) 🤝")
        print(f"{G}[3]{W} Automated Password Bypass/Crack 🔓")
        print(f"{G}[4]{W} Exit ❌")
        
        choice = input(f"\n{C}Select Option > {W}")
        
        if choice == '1': scan_wifi(); input("\nPress Enter to continue...")
        elif choice == '2': capture_handshake(); input("\nPress Enter to continue...")
        elif choice == '3': bypass_crack(); input("\nPress Enter to continue...")
        elif choice == '4': break

if __name__ == "__main__":
    main()

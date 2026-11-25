from scapy.all import sniff
import subprocess
import os
import sys
from zeroconf import ServiceInfo, Zeroconf

program_path = os.path.abspath(sys.argv[0])

RED = "\033[91m"
RESET = "\033[0m"

from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

logo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⢠⡿⠀⠀⣀⡤⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⢃⣴⡿⠁⣠⣾⣯⣤⣴⣾⣿⣋⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣟⣵⣿⢏⣴⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣯⣾⣿⢧⣻⣿⡞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⢿⣿⣿⣿⣿⣝⣺⠟⠋⠉⠈⠉⠻⣿⣿⣿⣿⣿⣿⣿⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣤⣾⡿⣿⣿⣿⡿⠷⠖⠂⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡂⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣴⣠⣴⣿⣿⠿⣿⣧⣿⣿⠟⠛⠓⠀⠀⠀⠀⠀⠀⣸⣽⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣧⣿⡿⠅$$ ⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣚⠿⣷⣿⣿⣿⣿⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠿  $$ ⣴⣿⠀⠀⠀⠀⠀⠀⠀⢀⠺⣿⡿⣱⣿⣿⣿⣿⠃⠠⠃⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  $$$ ⠈⠙⠛  ⠀⠀⠀⠀⠀⣴⣿⣿⡗⣼⣿⣿⣿⣿⣿⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
$$$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣦⣭⣽⢸⣿⣿⣿⣿⣯⠘⠇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
$$⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢿⣿⡏⣿⣿⣿⣿⣿⣿⣷⣖⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print( RED + logo + RESET)
print("Tool made by", RED + "-777" + RESET)
print("=============")
print("[1] Trafic capture")
print("=============")
if os.geteuid() != 0:
    print(RED + f'[!] Run with: sudo {sys.executable} {os.path.abspath(sys.argv[0])}' + RESET)
    input("\nPress Enter to exit...")
    sys.exit()
choice = input(": ")
if choice == "1" or choice == "Trafic capture":
    print("[1] ICMP")
    print("[2] TCP")
    print("[3] UDP")
    print("[4] HTTP")
    print("[5] HTTPS")
    print("[6] DNS")
    print("[7] ALL")
    target_ip = input("Target IP: ")
    protocol = input("Choose protocol: ")

    protocols = {
        "1": "icmp",
        "2": "tcp",
        "3": "udp",
        "4": "tcp port 80",
        "5": "tcp port 443",
        "6": "port 53",
        "7": None,
    }
    filter = protocols.get(protocol)
    filter = f"host {target_ip} and {filter}"
    print(filter)
if protocol == "1":

    print( RED + "[!] ICMP selected" + RESET)

elif protocol == "2":

    print(RED + "[!] TCP selected" + RESET)

elif protocol == "3":

    print(RED + "[!] UDP selected" + RESET)
elif protocol == "4":
    print(RED + "[!] HTTP selected" + RESET)
elif protocol == "5":
    print(RED + "[!] HTTPS selected" + RESET)
elif protocol == "6":
    print(RED + "[6] DNS selected" + RESET)

elif protocol == "7":

    print("[!] ALL selected")
print( RED + "[!] PRESS CTRL + C TO STOP CAPTURİNG" + RESET)
sniff(
    prn=packet_handler,
    store=False,
    filter=filter
)

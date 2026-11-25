# Network framework
from scapy.all import sniff
import requests
import socket

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def print_gradient_ascii(ascii_art):
    lines = ascii_art.splitlines()
    total_lines = len(lines)
    if total_lines == 0:
        return

    for line_idx, line in enumerate(lines):
        if line_idx < total_lines / 2:
            ratio = line_idx / (total_lines / 2) if total_lines > 1 else 1
            r = 0
            g = 255
            b = int(255 * ratio)
        else:
            ratio = (line_idx - total_lines / 2) / (total_lines / 2) if total_lines > 1 else 1
            r = 0
            g = int(255 * (1 - ratio))
            b = int(255 - (116 * ratio))

        print(f"\033[38;2;{r};{g};{b}m{line}\033[0m")

captured_packets = []


def packet_handler(pkt):
    summary_text = pkt.summary()
    captured_packets.append(pkt)  # İleride dosyaya yazmak için saklıyoruz
    print_gradient_ascii(summary_text)


def start_capture(count_limit=10, timeout_limit=2):
    print_gradient_ascii('Press CTRL + C to stop.')
    try:
        # sniff her paket yakaladığında packet_handler'ı tetikler
        sniff(prn=packet_handler, count=count_limit, timeout=timeout_limit)
    except PermissionError:
        print_gradient_ascii('Permission Required please run with sudo.')
        return
    except KeyboardInterrupt:
        print_gradient_ascii('Traffic capture has been stopped.')


art = """⠀⠀⣠⡴⠾⠛⠛⠛⠛⠛⠛⠳⠶⣤⣀⠀⠀⠀
⡠⠊⠁⢀⣤⡴⣾⣿⣿⣷⢶⣤⣀⠀⠈⠑⠦⡀
⣀⣴⣾⠛⠁⠀⣿⣿⣿⣿⠀⠈⠙⢳⣤⣀⡀⢈
⠉⠛⢦⣄⣀⡀⠙⠛⠛⠋⢀⣀⣠⠴⠛⠛⠓⠈
⠀⠀⠀⣹⢿⣏⠉⠉⠉⠉⠉⠀⣀⣀⣀⠀⠀⠀
⠀⠀⠰⣿⠀⠻⣧⡀⠀⠀⠀⠸⣏⡠⠉⣷⠀⠀
⠀⠀⠀⠋⠀⠀⠈⠻⢦⣄⣀⠀⠉⢀⣠⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠋⠉⠁⠀⠀⠀
[Network KQpi & Network framework &]
"""

menu = """
(01) Find devices
(02) ARP spoofing
(03) Firewall defense bypass
(04) Traffic capture
(05) DoS                
(06) Reverse DNS
(07) DNS
(08) Port scan                                  

(99) About the project & github
"""

choice_map = {
    "01" : "Finding devices",
    "02" : "ARP spoofing",
    "03" : "Firewall defense bypass",
    "04" : "Traffic capture",
    "05" : "DoS",
    "06" : "Reverse DNS",
    "07" : "DNS",
    "08" : "Port scan",

    "99" : "About the project & Github"
}

print_gradient_ascii(art)
print_gradient_ascii(menu)

while True:
    choice = input('Net_(KTP)\nÇ$: ')

    choice = choice.split(' ')

    if len(choice) > 0 and (choice[0] == '04' or choice[0] == '4'):
        print_gradient_ascii('Capturing....')

        count_val = int(choice[2]) if len(choice) > 2 else 10

        start_capture(count_limit=count_val)

        save_ = input('Do u want to save the file? (y/n): ')
        if save_.lower() == 'y':
            with open('save.txt', 'a', encoding='utf-8') as f:
                for p in captured_packets:
                    f.write(str(p.summary()) + '\n')
            print_gradient_ascii('Save file has been saved.')
            print_gradient_ascii('Thank you for using Medusa NETkpqi.')

    elif len(choice) > 0 and (choice[0] == '05' or choice[0] == '5'):
        print('=== DoS assisted with threads ===')
        try:
            ip = choice[1]
            amount = int(choice[2]) if len(choice) > 2 else 10
        except IndexError:
            print(RED + 'Invalıd option aborting option type --help for commands' + RESET)
            break

        for i in range(amount):
            response_code = requests.post(ip)
            print(GREEN + f" Request has ben sent [{response_code}]" + RESET)


    elif len(choice) > 0 and (choice[0] == '07' or choice[0] == '7'):
        try:
            print('=== DNS ===')
            domain = choice[1]
            dns = socket.gethostbyname(domain)
            print(GREEN + f'found : {dns}' + RESET)

        except socket.gaierror:
            print(RED + 'Could not reverse dns socket.gaierror' + RESET)

    elif len(choice) > 0 and (choice[0] == '06' or choice[0] == '6'):
        print('=== Reverse DNS ===')
        try:
            ip = choice[1]
            rvr = socket.gethostbyaddr(ip)
            print(GREEN + f'Domain found : {rvr}' + RESET)
        except socket.gaierror:
            print(RED + 'Could not reverse dns socket.gaierror' + RESET)

    elif choice not in choice_map:
        print_gradient_ascii('Unknow command please type --help for command options')

    elif choice[0] == '':
        print('?')
        continue






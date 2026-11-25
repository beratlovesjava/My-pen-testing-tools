#!/usr/bin/env python3
import os
import sys
import requests
import time
from bs4 import BeautifulSoup
import re
import concurrent.futures
from scapy.all import sniff
import socket
import webbrowser

def spiderweb():
    try:
        ip = input(KOYU_KIRMIZI + "[?] Enter IP: " + RESET)
        port = input(KOYU_KIRMIZI + "[?] Enter port: " + RESET)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.listen(1)
        print("[?] Listening to....", ip, port)
        print(KOYU_KIRMIZI + "[:)] Do Ctrl + c to stop listening" + RESET)

        conn, addr = s.accept()
        print(KOYU_KIRMIZI + "[!] Connection from:", addr + RESET)

        data = conn.recv(1024)
        print(KOYU_KIRMIZI + RESET, "[FOUND] ", data)
    except OSError:
        print(KOYU_KIRMIZI + "[#] Port is already in use or no permission." + RESET)
    except ConnectionRefusedError:
        print(KOYU_KIRMIZI + "[#] Connection refused server is probably closed." + RESET)
    except KeyboardInterrupt:
        print(KOYU_KIRMIZI + "[#] Listening was stopped by user" + RESET)
        s.close()
    except TimeoutError:
        print(KOYU_KIRMIZI + "[#] Timeout error." + RESET)
    except ConnectionResetError:
        print(KOYU_KIRMIZI + "[#] Connection was reseted." + RESET)

def grab_banner(ip, common_ports, timeout=2):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((ip, common_ports))

        if result == 0:
            try:
                banner = s.recv(4096).decode(errors='ignore').strip()
            except Exception:
                banner = ''
            print(KOYU_KIRMIZI + f'===================\n'
                                 f'|port: {common_ports}\n'
                                 f'|status: [OPEN]\n'
                                 f'|service:  {banner}' + RESET)
        else:
            pass

        s.close()

    except socket.gaierror:
        print(KOYU_KIRMIZI + '[-] İnvalid ip' + RESET)
    except TimeoutError:
        print(KOYU_KIRMIZI + '[-] Socket timeout error' + RESET)
    except ConnectionResetError:
        print(KOYU_KIRMIZI + '[-] Connection reset error' + RESET)
    except ConnectionRefusedError:
        print(KOYU_KIRMIZI + f'[-] Port refused connection {common_ports} ' + RESET)

common_ports = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 111, 123, 135, 137, 138, 139, 143, 161, 162,
    179, 389, 443, 445, 465, 514, 587, 631, 636, 873,
    1900, 1433, 1434, 1521, 3306, 5432, 5984, 6379, 9200, 9300,
    11211, 27017, 27018, 2049, 2222, 3389, 5900, 5901, 591, 800,
    808, 1080, 1723, 3128, 3690, 5000, 5601, 6667, 6881, 8000,
    8008, 8080, 8081, 8443, 8888, 9000, 9090, 9999, 2375, 2376,
    6443, 10250, 4444, 5353, 5355
]

choice_map_portscan_spiderweb = {
    "--help": "shows options",
    "spiderweb $scan_all": "scan all the common ports",
    "spiderweb $goback":"go back to the menu",

}


def port_Scan_console_spiderweb():
    print(KOYU_KIRMIZI + '[!] Please type spiderweb $goback for going back to the original menu' + RESET)
    while True:
        command = input(KOYU_KIRMIZI + 'SpiderWeb(Portscan_console): ' + RESET)

        if command == '--help':
            print(KAPALI_SARI + '____________' + RESET)
            print(KOYU_KIRMIZI + 'Active Modules:\n'
                                 'spiderweb $scan_all - Scanning all common ports\n'
                                 'spiderweb $goback - Going back to the menu\n'
                                 'spiderweb $q - Quit\n'
                                 'spiderweb $show_scannable_port_modules - Shows all the common ports' + RESET)
            print(KAPALI_SARI + '____________' + RESET)
        elif command == '':
            continue

        elif command not in choice_map_portscan_spiderweb:
            print(KOYU_KIRMIZI + '[+] SpiderWeb port scan could not find command try --help to see options...' + RESET)

        elif command == 'spiderweb $scan_all':
            ip = input('Target IP: ')
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                for port in common_ports:
                    executor.submit(grab_banner, ip, port)
        elif command == 'spiderweb $q':
            break
        elif command == 'spiderweb $goback':
            return

        elif command == 'spiderweb $show_scannable_port_modules':
            print(KOYU_KIRMIZI + common_ports + RESET)




common_ports_menu = """

  Common Ports Reference - SpiderWeb

  Core Services
    20 FTP-data   21 FTP      22 SSH       23 Telnet    25 SMTP
    53 DNS        67 DHCP     68 DHCP      69 TFTP      80 HTTP
    110 POP3      111 RPC     123 NTP      135 MS-RPC   137-139 NetBIOS
    143 IMAP      161 SNMP    162 SNMP     179 BGP      389 LDAP
    443 HTTPS     445 SMB     465 SMTPS    514 Syslog   587 SMTP-sub
    631 IPP       636 LDAPS   873 rsync    1900 UPnP

  Databases
    1433-34 MSSQL    1521 Oracle    3306 MySQL     5432 PostgreSQL
    5984 CouchDB     6379 Redis     9200-300 Elastic   11211 Memcached
    27017-18 MongoDB

  Remote Access
    2049 NFS     2222 SSH-alt   3389 RDP    5900-01 VNC

  Web / Proxy / App Servers
    591 FileMaker   800 808      1080 SOCKS    1723 PPTP
    3128 Squid      3690 SVN     5000 Flask    5601 Kibana
    6667 IRC        6881 BitTorrent   8000 8008  8080 8081 HTTP-alt
    8443 HTTPS-alt  8888 Jupyter 9000 PHP-FPM  9090 Prometheus
    9999 misc

  Containers / Orchestration
    2375-76 Docker   6443 K8s-API   10250 Kubelet

  Other
    4444 Metasploit   5353 mDNS   5355 LLMNR
"""

def show_help():
    print(BEYAZ + """
Usage: spiderweb <module> [target]

Modules:
  1, sql        SQL injection vulnerability test        (spiderweb> 1)
  2, hidden     Hidden URL / endpoint discovery          (spiderweb> 2)
  3, dir        Directory brute-force scan (threaded)    (spiderweb> 3)
  4, poison     Counter-poisoning (fake data flood)      (spiderweb> 4)
  5, scrape     Web scraper / keyword finder             (spiderweb> 5)
  6, sniff      Traffic capture (ICMP/TCP/UDP)            (spiderweb> 6)
  7, XSS        XSS vulnerability scan                    (spiderweb> 7)
  8, dns        Reverse DNS lookup                       (spiderweb> 8)
  9, portscan   Threading assisted port scan             (spiderweb> 9)
  10,netcat     İp and port listener                     (spiderweb> 10)
  
  99,github     777s github repository for this project (spiderweb> 99)

Other commands:
  --help        Show this menu
  clear         Clear the screen
  exit          Quit SpiderWeb
  q             exit SpiderWeb
  --scanabbleports show common ports

Examples:
  spiderweb> 1
  spiderweb> portscan
""")

if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-256color'

# --- SPIDERWEB PROFESYONEL PENTEST RENKLERİ ---
RESET = "\033[0m"
MOR = "\033[38;2;88;35;117m"
BEYAZ = "\033[1;37m"
GRI = "\033[38;2;120;120;120m"
KAPALI_SARI = "\033[38;2;180;140;0m"  # sqlmap warning / bilgi logu tonu
KOYU_KIRMIZI = "\033[38;2;139;0;0m"  # Zafiyet / kritik hata tonu
KOYU_CYAN = "\033[38;2;0;139;139m"  # "dark cyan" / deniz mavisi tonu
CYAN = "\033[38;2;0;255;255m"

sql_example = 'https://example.com'
sql_example2 = 'http://example.com'


def show_spiderweb_cli():
    ascii = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⠤⠶⠶⢶⠶⣼⣿⣿⣿⣿⣿⣠⡴⢤⠤⠤⣄⣀⠀⠀
⠐⣋⡥⠶⠒⠛⠙⠳⣝⣿⣿⣿⣿⣿⣿⠞⠛⠒⠶⢤⣩⠳⠀
⠜⠉⠀⠀⣠⠖⠛⢒⠾⢿⣿⣿⣿⡯⠤⠖⠒⢦⡀⠀⠈⠳⡄
⠀⠀⣠⠟⠁⠐⡞⠛⠉⢩⢿⢿⣏⠛⠓⢒⣆⠀⠙⢧⡀⠀⠀
⠀⢸⠃⠀⠀⠀⢱⡀⠀⠀⠃⠀⠁⠀⠀⣼⠁⠀⠀⠈⢷⠀⠀
⠀⠈⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(
        KOYU_KIRMIZI + "[!] We do not take responsibility if SpiderWeb is used for bad purposes it was meant for CTF and ethical web security Blue team & Red team" + RESET)
    print(KOYU_KIRMIZI + "SpiderWeb v2.0.8-stable - Automated Web & Network Exploitation Framework" + RESET)
    print(KOYU_KIRMIZI + ascii + RESET)
    print(KAPALI_SARI + "[*] Initialize crawler threads... Connection handshake successful." + RESET)
    print(GRI + f"[*] Local system check: {os.name.upper()} | Python {sys.version.split()[0]}" + RESET)
    print(KOYU_KIRMIZI + "─" * 74 + RESET)
    print(BEYAZ + "Active Modules:" + RESET)
    print(f"  {KOYU_KIRMIZI}[01]{RESET} SQL injection database vulnerability mapper")
    print(f"  {KOYU_KIRMIZI}[02]{RESET} Hidden endpoint and URL resource discovery engine")
    print(f"  {KOYU_KIRMIZI}[03]{RESET} Open web directories multi-threaded brute-forcer")
    print(f"  {KOYU_KIRMIZI}[04]{RESET} Fake data for destroying phishing sites (Counter-Poisoning)")
    print(f"  {KOYU_KIRMIZI}[05]{RESET} Web scraper for CTF and ethical web security")
    print(f"  {KOYU_KIRMIZI}[06]{RESET} Trafic capture & network exploitation framework")
    print(f"  {KOYU_KIRMIZI}[07]{RESET} XSS vulnerability scan")
    print(f"  {KOYU_KIRMIZI}[08]{RESET} Reverse DNS")
    print(f"  {KOYU_KIRMIZI}[09]{RESET} Threading assisted port scan")
    print(f"  {KOYU_KIRMIZI}[10]{RESET} NetCat alternetice port and ip listener")
    print(KOYU_KIRMIZI + "─" * 74 + RESET)
    print(f"  {KOYU_KIRMIZI}[99]{RESET} Github")
    print(KAPALI_SARI + "[+] SpiderWeb engine ready. Enter a module number to proceed." + RESET + "\n")

def url_to_ip():
    try:
        url = input(KOYU_KIRMIZI + '[?] Enter url: ' + RESET)

        ip = socket.gethostbyname(url)
        print('=== SpiderWeb reverse DNS ===')
        print(KOYU_KIRMIZI + '[+] IP has been found : ', ip, url + RESET)
        print(KOYU_KIRMIZI + '[?] Do you want SpiderWeb to take you to', url + RESET)
        choice = input('[y/N]\n'
                       '|: ')
        if choice == 'y' or choice == 'Y':
            webbrowser.open(url)
        elif choice == 'n' or choice == 'N':
            print(GRI + '[-] Scan completed returning back to menu....', url + RESET)


    except socket.gaierror:
        print(KOYU_KIRMIZI + '[-] Could not resolve to the host' + RESET)

def scan_port(ip,port):


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip,port))

        if result == 0:
            print(KOYU_KIRMIZI + f'[+] OPEN : {port}' + RESET)
        else:
            print(KOYU_KIRMIZI + f"[-] CLOSED {port}" + RESET)

        s.close()

    except socket.gaierror:
        print(KOYU_KIRMIZI + '[-] Please enter a valid IP')

    except TimeoutError:
        print(KOYU_KIRMIZI + '[-] Timeout error' + RESET)

    except OSError:
        print(KOYU_KIRMIZI + '[-] Socket refused' + RESET)


def thread():
    ip = input('[+] Target IP: ')
    ports_str = input('[+] Ports : ')
    ports = [int(p) for p in ports_str.split(',')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for p in ports:
            executor.map(scan_port, ip, ports)



def uhuh():
    # Özel Renk Paleti (RGB TrueColor - Tamamen Koyu & Agresif)
    RESET = "\033[0m"
    DARK_RED = "\033[38;2;139;0;0m"  # Koyu Kan Kırmızısı (Banner ve başlıklar için)
    DARK_YELLOW = "\033[38;2;150;110;0m"  # Koyu Sarı / Hardal (Seçenekler ve uyarılar için)
    BEYAZ = "\033[1;37m"
    GRI = "\033[38;2;100;100;100m"

    def packet_handler(paket):
        print(f"{GRI}[+] Captured:{RESET} {BEYAZ}{paket.summary()}{RESET}")

    print(f"{DARK_RED}=== SpiderWeb trafic capture ==={RESET}")
    print(f"{DARK_RED}==============================={RESET}")
    print(f"{DARK_YELLOW}[01]{RESET} {BEYAZ}ICMP (Ping){RESET}")
    print(f"{DARK_YELLOW}[02]{RESET} {BEYAZ}TCP{RESET}")
    print(f"{DARK_YELLOW}[03]{RESET} {BEYAZ}UDP{RESET}")
    print(f"{DARK_RED}==============================={RESET}")

    choice = input(f"{DARK_YELLOW}[+] Choose an option: {BEYAZ}")
    print(RESET, end="")

    target = input(f"{DARK_YELLOW}[+] Enter target (bos birakmak icin enter): {BEYAZ}")
    print(RESET, end="")

    amount_input = input(f"{DARK_YELLOW}[+] Amount: {BEYAZ}")
    print(RESET, end="")

    try:
        amount = int(amount_input)
    except ValueError:
        amount = 10  # Hatalı giriş olursa varsayılan miktar

    filtre = ""
    if choice in ["1", "ICMP", "icmp", "ıcmp", "Ping", "ping", "01"]:
        filtre = "icmp"
    elif choice in ["2", "TCP", "tcp", "02"]:
        filtre = "tcp"
    elif choice in ["3", "UDP", "udp", "03"]:
        filtre = "udp"
    else:
        print(f"{DARK_RED}[-] İnvalid choice ICMP was automatically selected.{RESET}")
        filtre = "icmp"

    final_filter = filtre
    if target:
        clean_target = target.replace('http://', '').replace('https://', '').split(':')[0]
        final_filter = f"{filtre} and host {clean_target}"

    print(
        f"\n{DARK_YELLOW}[*] Listening..{RESET} {GRI}Filtre:{RESET} {BEYAZ}{final_filter}{RESET} {GRI}| Adet:{RESET} {BEYAZ}{amount}{RESET}\n")

    # Dinlemeyi başlat
    sniff(filter=final_filter, prn=packet_handler, count=amount)

    print(f"\n{DARK_RED}[+] Packet Filtered {RESET}")


def scraping():
    url = input(KOYU_KIRMIZI + 'Enter URL: ' + RESET).strip()
    if not url:
        print(KOYU_KIRMIZI + "[-] [ERROR] URL cannot be empty!" + RESET)
        return

    try:
        html = requests.get(url, timeout=5).text
    except Exception as e:
        print(KOYU_KIRMIZI + f"[-] [ERROR] Could not fetch URL: {e}" + RESET)
        return

    soup = BeautifulSoup(html, 'html.parser')

    print('=== SpiderWeb web scraper ===')
    print(KOYU_KIRMIZI + '[01] Secret notes / Keyword finder' + RESET)
    print(KOYU_KIRMIZI + '[02] Show source code' + RESET)
    print('')

    choice = input('Pick option: ').strip()

    if choice == '1':
        print(BEYAZ + f'=== Scraping... {url} Please wait ===' + RESET)
        wordlist = ['admin', 'log', 'robots.txt', 'a', 'input', 'token', 'secret', 'key', 'admin_log']
        pattern = re.compile('|'.join(wordlist), re.IGNORECASE)
        find = soup.find_all(string=pattern)

        print(KOYU_KIRMIZI + f'\n[+] Scan has completed total {len(find)} words have been found' + RESET)

        for sonuc in find:
            temiz_metin = sonuc.strip()
            if temiz_metin:
                print(KAPALI_SARI + f'\n[+] Scraping [FOUND] :  {temiz_metin}' + RESET)
                start_time = time.time()
                try:
                    res = requests.get(f"{url.rstrip('/')}/{temiz_metin}", timeout=2.5)
                    if res.status_code == 200:
                        print(BEYAZ + f"    [FOUND content]: {res.text[:100].strip()}..." + RESET)
                except requests.exceptions.Timeout:
                    pass
                except requests.exceptions.ConnectionError:
                    print(KOYU_KIRMIZI + f'[-] Could not connect to subpath' + RESET)

                elapsed_time = time.time() - start_time
                print(GRI + f'[*] Sub-request completed in {elapsed_time:.2f} seconds' + RESET)

    elif choice == '2':
        print(f'\n--- Source Code of {url} ---\n')
        print(soup.prettify()[:1000] + "\n[... truncated for display ...]")


def connect_to_tor():
    session = requests.Session()
    tor_proxy = 'socks5h://127.0.0.1:9050'
    session.proxies = {'http': tor_proxy, 'https': tor_proxy}
    return session


def check_single_url(http_adresi):
    """Thread havuzu için tekil URL kontrol fonksiyonu"""
    try:
        response = requests.get(http_adresi, timeout=3, allow_redirects=False)
        if response.status_code == 200:
            print(KOYU_KIRMIZI + f'[+] {http_adresi} [OPEN] {response.status_code}' + RESET)
        elif response.status_code == 404:
            pass  # 404'leri kalabalık yapmasın diye gizledik, dilersen açabilirsin
        elif response.status_code == 403:
            print(KOYU_KIRMIZI + f'[-] {http_adresi} [FORBIDDEN] Directory exists but no access (403)' + RESET)
        elif response.status_code in [301, 302]:
            print(KOYU_KIRMIZI + f'[-] {http_adresi} [REDIRECT] Needs access/moved ({response.status_code})' + RESET)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        pass


def directory_scan():
    print('=== SpiderWeb directory scan ===')
    http_adresi = input(KOYU_KIRMIZI + '[?] Enter target URL: ' + RESET).strip()

    if not http_adresi.startswith('http://') and not http_adresi.startswith('https://'):
        print('[-] Invalid Url please try again')
        return

    test_urls = ['admin', 'login', 'robots.txt', 'a', 'db', 'input', 'dashboard', 'secret', 'test']
    urls_to_scan = [f'{http_adresi.rstrip("/")}/{w}' for w in test_urls]

    print(GRI + f'[*] Scanning {len(urls_to_scan)} endpoints with multi-threading...' + RESET)
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_single_url, urls_to_scan)

    elapsed_time = time.time() - start_time
    print(GRI + f'[*] Scanning completed in {elapsed_time:.2f} seconds' + RESET)


def counter_poisoning():
    print(KOYU_KIRMIZI + "\n=== [SpiderWeb - Counter-Poisoning / Fake Data Flood] ===" + RESET)
    target = input(KAPALI_SARI + "[?] Enter target phishing/malicious URL: " + RESET).strip()
    if not target:
        print("[-] URL cannot be empty.")
        return

    print(GRI + "[*] Preparing fake traffic payload..." + RESET)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    payloads = {'username': 'fake_user_spiderweb', 'password': 'random_password_12345'}

    try:
        print(GRI + "[*] Flooding fake requests to disrupt logs..." + RESET)
        for i in range(5):
            requests.post(target, data=payloads, headers=headers, timeout=3)
        print(KAPALI_SARI + "[+] Counter-poisoning batch successfully sent." + RESET)
    except Exception as e:
        print(KOYU_KIRMIZI + f"[-] Error sending flood requests: {e}" + RESET)


def sql_injection():
    print(KOYU_KIRMIZI + "\n=== [SpiderWeb - SQL Injection Vulnerability Mapper] ===" + RESET)
    print(GRI + f"[*] Examples: {sql_example2} | {sql_example}" + RESET)
    sql_ = input(KAPALI_SARI + "[?] Enter target URL for injection test: " + RESET).strip()

    if not sql_:
        print(KOYU_KIRMIZI + "[-] [ERROR] URL cannot be empty!" + RESET)
        return

    if not sql_.startswith('https://') and not sql_.startswith('http://'):
        print(KOYU_KIRMIZI + "[-] [ERROR] Enter a valid URL starting with http:// or https://" + RESET)
        return

    sql_errors = [
        'you have an error in your sql syntax',
        'warning: mysql_fetch_array()',
        'unclosed quotation mark after the character string',
        'pg_query(): query error:'
    ]

    test_url = sql_ + "'"
    print(GRI + f"[*] Injecting malicious payloads to: {test_url}" + RESET)

    try:
        response = requests.get(test_url, timeout=5)
        page_content = response.text.lower()
        is_there_vulnerability = False

        for error in sql_errors:
            if error in page_content:
                is_there_vulnerability = True
                break

        if is_there_vulnerability:
            print(KOYU_KIRMIZI + f"[!] [CRITICAL] SQL Injection Vulnerability Found! Target looks vulnerable." + RESET)
        else:
            print(GRI + "[-] [INFO] No SQL database error patterns detected in response." + RESET)

    except requests.exceptions.ConnectionError:
        print(KOYU_KIRMIZI + "[-] [ERROR] Could not connect to the remote host." + RESET)
    except requests.RequestException:
        print(KOYU_KIRMIZI + "[-] [ERROR] Request timed out." + RESET)


def show_hidden_urls():
    print(KOYU_KIRMIZI + "\n=== [SpiderWeb - Hidden URL Endpoint Scanner] ===" + RESET)
    hedef_url = input(KAPALI_SARI + "[?] Enter target URL: " + RESET).strip()

    if not hedef_url:
        print(KOYU_KIRMIZI + "[-] [ERROR] Please enter a valid URL." + RESET)
        return

    if not (hedef_url.startswith('http://') or hedef_url.startswith('https://')):
        print(KOYU_KIRMIZI + f"[-] [ERROR] The URL '{hedef_url}' is not valid." + RESET)
        return

    wordlists = {
        "admin", "login", "config", "db", "api", "secret", "backup",
        "robots.txt", "dashboard", "phpmyadmin", "mysql", "user",
        "uploads", "index.php", "staging", "dev", "test", "wp-admin"
    }

    print(GRI + f"[*] Launching path traversal... Auditing {len(wordlists)} potential paths." + RESET)
    headers = {'User-Agent': 'spiderweb-scanner/1.0'}
    bulunan_sayisi = 0

    for kelime in wordlists:
        test_url = f"{hedef_url.rstrip('/')}/{kelime}"
        try:
            response = requests.get(test_url, headers=headers, timeout=3, allow_redirects=False)
            if response.status_code == 200:
                print(
                    KAPALI_SARI + f"[+] [FOUND] Hidden resource endpoint: /{kelime} -> (HTTP {response.status_code})" + RESET)
                bulunan_sayisi += 1
        except requests.RequestException:
            pass

    print(KAPALI_SARI + f"[*] Scan finished. {bulunan_sayisi} hidden resource(s) mapped successfully." + RESET)


# --- ANA PROGRAM INTERAKTIF PROGRAM DÖNGÜSÜ ---
choice_map = {
    '1': 'SQL database test',
    '2': 'Show hidden Urls',
    '3': 'Show web directorys',
    '4': 'Counter-Poisoning',
    '5': 'Scraper',
    '6': 'Trafic capturing',
    '7': 'Xss vulnerability scan',
    '8': 'Reverse DNS',
    '9' : 'Scan port',
    '10': 'İp and port listener',

    '99': 'Github repo of this projects'
}

# Başlangıç ekranını bir kere temizleyip menüyü basıyoruz
os.system('cls' if os.name == 'nt' else 'clear')
show_spiderweb_cli()

while True:
    try:
        command = input(
            KOYU_KIRMIZI + "spiderweb" + BEYAZ + "(" + KAPALI_SARI + "interactive" + BEYAZ + ") > " + RESET).strip()

        if not command:
            continue

        if command == 'exit':
            print(KAPALI_SARI + "[*] Shutting down SpiderWeb framework engine..." + RESET)
            break

        elif command == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            show_spiderweb_cli()
            continue

        elif command == '1' or command == '01':
            sql_injection()
            print("")

        elif command == '2' or command == '02':
            show_hidden_urls()
            print("")

        elif command == '3' or command == '03':
            directory_scan()
            print("")

        elif command == '4' or command == '04':
            counter_poisoning()
            print("")

        elif command == '5' or command == '05':
            scraping()
            print("")

        elif command == '6' or command == '06':
            uhuh()

        elif command == '7' or command == '07':
            print('hello world')

        elif command == '8' or command == '08':
            url_to_ip()

        elif command == '9' or command == '09':
            thread()

        elif command == "10" or command == "netcat":
            spiderweb()

        elif command == "--help" or command == "command list":
            show_help()

        elif command == "--scanabbleports" or command == "common port list":
            print(CYAN + common_ports + RESET)

        elif command == "q" or command == "quit" or command == "exit spiderweb" or command == "quit spiderweb":
            break

        elif command == "portscan" or command == "spiderweb portscan command_line":
            port_Scan_console_spiderweb()

        elif command == "99" or command == "github":
            github = "https://github.com/beratlovesjava/Learning-tools-and-projects-Java-Python-"
            webbrowser.open(github)

        else:
            print(KOYU_KIRMIZI + f"[-] [ERROR] Unknown command or module index: '{command}'" + RESET)


    except KeyboardInterrupt:
        print(KAPALI_SARI + "\n[*] User aborted operation. Type 'exit' to terminate engine gracefully." + RESET)

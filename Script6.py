import requests
from bs4 import BeautifulSoup
import re
import time
import datetime

RESET = "\033[0m"
MOR = "\033[38;2;88;35;117m"
BEYAZ = "\033[1;37m"
GRI = "\033[38;2;120;120;120m"
KAPALI_SARI = "\033[38;2;180;140;0m"  # sqlmap warning / bilgi logu tonu
KOYU_KIRMIZI = "\033[38;2;139;0;0m"  # Zafiyet / kritik hata tonu


def scraping():
    url = input(KOYU_KIRMIZI + 'Enter URL: ' + RESET)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    print('=== SpiderWeb web scraper ===')
    print(KOYU_KIRMIZI +'[01] Secret notes' + RESET)
    print(KOYU_KIRMIZI + '[02] Show source code' + RESET)
    print('')
    try:
        choice = input('Pick option: ')
    except ValueError:
        print('[-] Please enter a valid option')

    if choice == '1':
        print(BEYAZ + f'=== Scraping...{url} Please wait ===' + RESET)
        wordlist = ['admin', 'log', 'robots.txt', 'a', 'input', 'token', 'secret', 'key', 'admin_log']

        pattern = re.compile('|'.join(wordlist), re.IGNORECASE)

        find = soup.find_all(string=pattern)

        print(KOYU_KIRMIZI + f'\n[+] Scan has completed total {len(find)} words have been found' + RESET)

        for sonuc in find:
            temiz_metin = sonuc.strip()
            if temiz_metin:
                print(KAPALI_SARI + f'\n[+] Scraping [FOUND] :  {sonuc.strip()}' + RESET)

    elif choice == '2':
        print(f'Source code of {url}...')
        soup.prettify()
scraping()
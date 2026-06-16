"""
Mr. Robot inspired OSINT username reconnaissance tool that 
checks for the existence of a given username across 
multiple popular platforms. 

Usage: python username_recon.py <username>
"""

import requests
import sys
import re
import time
import random
from colorama import Fore, Style, init

# Initialize color handling before any colored output is emitted.
init()

FSOCIETY_BANNER = r"""
  ▄█▀██▀█▄    ░█▀▀▀█░        ░█▀▀▀█░    ░█▀▀▀█░    ░█▀▀▀█▄    ░█▀▀▀█░    █▒░███  
▒ ░█ ██ █░ ▒▒ ▒█ ▒ █▒ ▒    ▒ ▒█ ▒ █▒ ▒▒ ▒█ ▒ █▒ ▒▒ ▒█ ░ █▒ ▒▒ ▒█ ▒ █▒ ▒▒▄▄ ▒█ ▄▄▒
█ ▒█ ██ █▒ ██ ▓█ ▓ █▓ █    █ ▓█ ▓ █▓ ██ ▓█ █ █▓ ██ ▓█ ▀ █▓ ██ ▓█ █ █▓ ████ ▓█ ███
░ ▓█ ██ █▓ ░░ ██ ▀ ██ ░    ░ ██ ▀ ██ ░░ ██ ░ ██ ░░ ██████▀ ░░ ██ ░ ██ ░░░░ ██ ░░░
▒ ██ ██ ██ ▒▒ ██████  ▒    ▒ ██████  ▒▒ ██ ▒ ██ ▒▒ ██ ▄ ██ ▒▒ ██ ▒ ██ ▒▒▒░ ██ ░▒▒
▓ ██ ██ ██ ▓▓ ██ ▄ ██ ▓    ▓ ██ ▄ ██ ▓▓ ██ ▓ ██ ▓▓ ██ ▓ █▓ ▓▓ ██ ▓ ██ ▓▓▓▒ ██ ▒▓▓
▒ ▓█ █▓ █▓ ▒▒ ▓█ ▒ █▓ ▒    ▒ ▓█ ▒ █▓ ▒▒ ▓█ ▒ █▓ ▒▒ ▓█ ▒ █▒ ▒▒ ▓█ ▒ █▓ ▒▒▒░ ▓█ ░▒▒
░ ▒█ █▒ █▒ ░░ ▒█ ░ █▒ ░    ░ ▒█ ░ █▒ ░░ ▒█ ░ █▒ ░░ ▒█ ░ █░ ░░ ▒█ ░ █▒ ░░░░ ▒█ ░░░
▀ ░█ █░ █░ ▀▀ ░█ ▀ █░ ▀    ▀ ░█ ▀ █░ ▀▀ ░█▄▄▄█░ ▀▀ ░█▄▄▄█▀ ▀▀ ░█▄▄▄█░ ▀▀▀▀ ░█ ▀▀▀
╭─╴╭─╮╭┬╮╭─╮╷ ╷╶┬╴╭─╴╭─╮   ╭─╮╭─╴╭─╮╭─╮╷╭─╮   ╷ ╷╷╶┬╴╷ ╷   ╭─╮   ╭─╮╭┬╮╷╷  ╭─╴
│  │ ││││├─╯│ │ │ ├╴ ├┬╯   ├┬╯├╴ ├─╯├─┤│├┬╯   │╷││ │ ├─┤   ├─┤   ╰─╮│││││  ├╴ 
╰─╴╰─╯╵ ╵╵  ╰─╯ ╵ ╰─╴╵╰╴   ╵╰╴╰─╴╵  ╵ ╵╵╵╰╴   ╰┴╯╵ ╵ ╵ ╵   ╵ ╵   ╰─╯╵ ╵╵╰─╴╰─╴
"""


def boot_beeps():
    print("\a")      # short beep
    time.sleep(0.2)
    print("\a")      # short beep
    time.sleep(0.5)
    print("\a")      # long beep


def decrypt_animation(text="Decrypting", duration=2.5, speed=0.02):
    charset = "█▓▒░<>/\\|!$%&#*"
    end_time = time.time() + duration

    while time.time() < end_time:
        fake = "".join(random.choice(charset) for _ in range(len(text) + 10))
        sys.stdout.write(Fore.GREEN + "\r" + fake + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(speed)

    sys.stdout.write(Fore.CYAN + f"\r{text}... DONE\n" + Style.RESET_ALL)
    sys.stdout.flush()


def type_out(text, delay=0.02):
    ansi_escape = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
    position = 0

    for match in ansi_escape.finditer(text):
        if match.start() > position:
            for char in text[position:match.start()]:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)

        sys.stdout.write(match.group())
        sys.stdout.flush()
        position = match.end()

    for char in text[position:]:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print()

type_out(Fore.RED + FSOCIETY_BANNER + Style.RESET_ALL, delay=0.0008)

SITES = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
}

def check_username(username):
    decrypt_animation("Decrypting system modules", duration=3)
    type_out(f"\n[+] Starting OSINT scan for: {username}\n", delay=0.01)
    time.sleep(0.5)

    for site, url in SITES.items():
        profile_url = url.format(username)
        try:
            response = requests.get(profile_url, timeout=5)

            if response.status_code == 200:
                type_out(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {site}: {profile_url}", \
                          delay=0.01)
            elif response.status_code == 404:
                type_out(f"{Fore.RED}[----]{Style.RESET_ALL} {site}: Not found", delay=0.01)
            else:
                type_out(f"{Fore.MAGENTA}[????]{Style.RESET_ALL} {site}: Unexpected status \
                         {response.status_code}", delay=0.01)

        except requests.exceptions.RequestException:
            type_out(f"{Fore.RED}[ERR!]{Style.RESET_ALL} {site}: Connection error", \
                     delay=0.01)

        
        time.sleep(0.2)

    boot_beeps()  # confirmation beep
    type_out(f"\n{Fore.CYAN}[+] Scan complete.{Style.RESET_ALL}\n", delay=0.01)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        type_out(f"{Fore.YELLOW}Usage:{Style.RESET_ALL} python username_recon.py <username>", \
                 delay=0.01)
        sys.exit(1)

    check_username(sys.argv[1])

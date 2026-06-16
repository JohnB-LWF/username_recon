"""
Mr. Robot inspired OSINT username reconnaissance tool that 
checks for the existence of a given username across 
multiple popular platforms. 

Usage: python username_recon.py <username>
"""

import requests
import sys
import re
import json
import time
import random
from colorama import Fore, Style, init

# Initialize color handling before any colored output is emitted.
init()

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
}

INSTAGRAM_HEADERS = {
    **REQUEST_HEADERS,
    "X-IG-App-ID": "936619743392459",
    "Referer": "https://www.instagram.com/",
    "Accept": "application/json",
}

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
    "GitHub": {
        "url": "https://github.com/{}",
        "headers": REQUEST_HEADERS,
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}/about.json",
        "headers": REQUEST_HEADERS,
    },
    "Twitter": {
        "url": "https://x.com/{}",
        "headers": REQUEST_HEADERS,
    },
    "Instagram": {
        "url": "https://www.instagram.com/api/v1/users/web_profile_info/?username={}",
        "headers": INSTAGRAM_HEADERS,
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "headers": REQUEST_HEADERS,
    },
}


def is_github_profile_found(response, username):
    return response.status_code == 200


def is_reddit_profile_found(response, username):
    if response.status_code != 200:
        return None

    try:
        payload = response.json()
    except ValueError:
        return None

    return (
        payload.get("kind") == "t2"
        and payload.get("data", {}).get("name", "").lower() == username.lower()
    )


def is_twitter_profile_found(response, username):
    if response.status_code != 200:
        return False

    text = response.text.lower()
    failure_markers = (
        "something went wrong",
        "javascript is not available",
        "this account doesn't exist",
        "account does not exist",
        "account suspended",
    )
    return not any(marker in text for marker in failure_markers)


def is_instagram_profile_found(response, username):
    if response.status_code != 200:
        return False

    try:
        payload = response.json()
    except ValueError:
        return False

    return payload.get("status") == "ok"


def is_tiktok_profile_found(response, username):
    if response.status_code != 200:
        return False

    match = re.search(
        r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',
        response.text,
    )
    if not match:
        return False

    try:
        payload = json.loads(match.group(1))
    except ValueError:
        return False

    profile_details = payload.get("__DEFAULT_SCOPE__", {}).get("webapp.user-detail", {})
    return profile_details.get("statusCode") == 0 and "userInfo" in profile_details


SITE_CHECKERS = {
    "GitHub": is_github_profile_found,
    "Reddit": is_reddit_profile_found,
    "Twitter": is_twitter_profile_found,
    "Instagram": is_instagram_profile_found,
    "TikTok": is_tiktok_profile_found,
}

def check_username(username):
    decrypt_animation("Decrypting system modules", duration=3)
    type_out(f"\n[+] Starting OSINT scan for: {username}\n", delay=0.01)
    time.sleep(0.5)

    for site, site_config in SITES.items():
        profile_url = site_config["url"].format(username)
        try:
            response = requests.get(
                profile_url,
                timeout=5,
                headers=site_config["headers"],
            )

            is_found = SITE_CHECKERS[site](response, username)

            if is_found is True:
                type_out(f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {site}: {profile_url}", \
                          delay=0.01)
            elif is_found is False or response.status_code == 404:
                type_out(f"{Fore.RED}[----]{Style.RESET_ALL} {site}: Not found", delay=0.01)
            else:
                type_out(f"{Fore.RED}[ERR!]{Style.RESET_ALL} {site}: Connection error", delay=0.01)

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

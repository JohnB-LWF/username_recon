# username_recon - Mr. Robot Inspired Python Script

## About

Just a small, flashy Python script inspired by the show Mr. Robot, with some ASCII art and animations for a fun cinema-themed hacking experience!

```
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
```

This script is a simple OSINT (open-source intelligence) tool for checking whether a username appears on multiple social media platforms. Run it with a username and it will check whether an account exists under the same name on the supported sites.

[Video Demo](https://www.youtube.com/watch?v=P4IYYiu8mPI)

[Read more on my blog](https://johnbelcher.dev/blog/entries/username-recon-python-script.html)

## Passive OSINT Tool

This tool performs passive OSINT by checking publicly available profiles.
It does not perform hacking, exploitation, or unauthorized access of any kind.

## Usage

Ensure you are using Python 3.

Install the dependencies listed in `requirements.txt`:

```PowerShell
pip install -r requirements.txt
```

Scan for a username:

```Python
python username_recon.py <username>
```

On Linux, use the equivalent commands:

```bash
pip3 install -r requirements.txt
python3 username_recon.py <username>
```

The script will then scan the predefined websites for the existence of that username and return the results.

## Platforms Checked

The script currently checks:

- GitHub
- Reddit
- Twitter/X
- Instagram
- TikTok

## Dependencies

The following Python packages are required:

- `colorama` for colored terminal output
- `requests` for standard HTTP requests
- `curl_cffi` for more browser-like request handling, especially for Reddit

## Bugs

Reddit may occasionally fail because Cloudflare sometimes requires browser-like challenge handling. In those cases, the script may return a connection error.

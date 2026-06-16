# Mr. Robot inspired Python Script

## Passive OSINT Tool

This tool performs passive OSINT by checking publicly available profiles.
It does not perform hacking, exploitation, or unauthorized access of any kind.

## About

This is a small, flashy script inspired by the show Mr. Robot.

## Usage

Ensure you are using Python 3.

Install the dependencies inside requirements.txt

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

The script will then scan the predefined websites for the existence of that username and return the results (found, not found).

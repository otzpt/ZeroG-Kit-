# zeroG-KIT

**Your pocket toolbox.** A CLI toolkit built to remove everyday friction from your computer workflow.

## The Problem

Every day there are small tasks that take longer than they should — converting an image, generating a password, checking if a file is safe, cleaning up temp files. Each one means opening a browser, installing a tool, or running a manual command. zeroG-KIT puts all of that into one place, from the terminal, instantly.

Every tool in here was chosen because it solves something I actually do manually on a regular basis.

## Tools

| # | Tool | Problem it solves |
|---|------|-------------------|
| 1 | Clean Temp & Prefetch | Manual cleanup of junk files takes too long |
| 2 | Clipboard History | No native way to see what's in your clipboard |
| 3 | Image Converter | Converting images usually requires a website or extra software |
| 4 | Password Generator | Most people reuse weak passwords because generating strong ones is annoying |
| 5 | Hash / Checksum | Verifying file integrity without opening a separate tool |
| 6 | Unit Converter | Stop googling "x kg to lbs" every time |
| 7 | QR Code Generator | Creating QR codes normally requires a website |
| 8 | Date & Time | Quick reference without alt-tabbing |
| 9 | System Info | Instant OS, RAM, CPU and disk snapshot |
| 10 | Password Strength | Know if your password is actually secure |
| 11 | Python Vulnerability Scanner | Quickly spot dangerous patterns in .py files |
| 12 | Encryption Tool | AES encrypt/decrypt text with a custom key |
| 13 | Firewall Assistant | Check if your firewall and RDP port are properly configured |
| 14 | Network Tools | Ping hosts, view local/public IP, check open ports, scan active IPs |

## Install

```bash
git clone https://github.com/otzpt/zeroG-KIT
cd zeroG-KIT
pip install -r requirements.txt
python main.py
```

> Note: Run as administrator for full functionality (temp cleanup, firewall checks).

## Built with

Python — `Pillow`, `psutil`, `qrcode`, `cryptography`, `hashlib`, `secrets`, `socket`

## What I learned

- How to structure a growing CLI toolkit across multiple files
- Python's `cryptography` library and how AES encryption works
- How to use `netsh` commands to check Windows firewall state
- How to use `re` (regex) to scan code for unsafe patterns
- How to use Python's `socket` module for network operations
- How to scan a local network with ping and filter active hosts
- Managing dependencies cleanly with `requirements.txt`

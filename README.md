# ZeroG-KIT

Your pocket toolbox. A Windows CLI toolkit built in Python — 20 tools organized into 5 categories, no bloat, no GUI dependency.

Built for the Hack Club Stardance "Frictionless" mission.

## Requirements

- Windows (uses `ctypes` for admin self-elevation, `netsh`, and other Windows-specific commands)
- Python 3.10+
- Dependencies in `requirements.txt`

```
pip install -r requirements.txt
```

## Running

```
python main.py
```

ZeroG-KIT auto-elevates to admin on launch (needed for temp cleanup, firewall checks, and some process operations).

## Structure

```
main.py          - entry point, category menus
utilities.py     - system, image, QR, password gen, unit converter, process tools
security.py      - hashing, password strength, encryption, vuln scan, firewall
network.py       - ping, IP lookup, port checker, LAN scanner
text_tools.py    - base64, JSON, case converter, regex tester, lorem ipsum
```

## Tools

### System Tools
- Clean Temp & Prefetch files
- View Clipboard history
- System Info (OS, RAM, CPU, disk)
- Process Killer — lists top 30 processes by memory usage, kill by name

### Utilities
- Image Converter (Pillow — convert between formats like png/jpg/bmp)
- QR Code Generator
- Unit Converter (temperature, weight, length, data size)
- Password Generator
- Date & Time

### Security
- Password Strength Checker
- Hash / SHA-256
- Encrypt / Decrypt (AES via Fernet)
- Python Vulnerability Scanner (flags eval, exec, os.system, subprocess, pickle.loads)
- Firewall Check (profile state + RDP port 3389 exposure)

### Network
- Ping host
- Local / Public IP lookup
- Port checker
- LAN active IP scanner

### Text & Data
- Base64 encoder/decoder
- JSON Formatter (pretty-print with validation)
- Case Converter (UPPER, lower, Title, camelCase, snake_case)
- Regex Tester
- Lorem Ipsum Generator

## Roadmap

- Menu polish: colorama colors, cleaner separators, version number in header
- GUI Edition (tkinter) — separate frontend sharing the same `utilities.py` logic, planned process killer with a kill button next to the live list

## Notes

This is a personal learning project built incrementally tool-by-tool, tracked via Hackatime as part of Hack Club Stardance.

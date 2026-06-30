import os
import re
import hashlib
import base64
from cryptography.fernet import Fernet


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def passwordCheck(password):
    criteria = [
        len(password) >= 12,
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[!@#$%^&*()]', password)),
    ]
    met = sum(criteria)
    if met >= 4:
        return "strong"
    elif met == 3:
        return "medium"
    else:
        return "weak"


def vulnChk(file_path):
    try:
        code = open(file_path).read()
    except FileNotFoundError:
        print("  Error: file not found")
        return
    checks = [
        ("eval(",        "eval() found - can execute arbitrary code"),
        ("exec(",        "exec() found - can execute arbitrary code"),
        ("os.system(",   "os.system() found - potential command injection"),
        ("subprocess",   "subprocess found - potential command injection"),
        ("pickle.loads(","pickle.loads() found - unsafe deserialization"),
    ]
    issues = [msg for pattern, msg in checks if pattern in code]
    if not issues:
        print("  No vulnerabilities found.")
    else:
        for issue in issues:
            print("  [!] " + issue)


def encrypt():
    while True:
        print("")
        print("  +---------------------------+")
        print("  |     ENCRYPTION TOOL       |")
        print("  +---------------------------+")
        print("  |  [1]  Encrypt text        |")
        print("  |  [2]  Decrypt text        |")
        print("  |  [0]  Back                |")
        print("  +---------------------------+")
        choice = input("  > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            text = input("  Text to encrypt: ")
            key = input("  Key: ")
            f = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))
            print("  Encrypted: " + f.encrypt(text.encode()).decode())
        elif choice == "2":
            text = input("  Text to decrypt: ")
            key = input("  Key: ")
            try:
                f = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))
                print("  Decrypted: " + f.decrypt(text.encode()).decode())
            except Exception:
                print("  Error: wrong key or invalid text")
        else:
            print("  invalid option")


def firewallChk():
    check = os.popen("netsh advfirewall show allprofiles state").read()
    print(check)
    if "OFF" in check:
        print("  [!] WARNING: Firewall is OFF in one or more profiles")
    else:
        print("  [OK] Firewall is ON in all profiles")

    rdp = os.popen("netsh advfirewall firewall show rule dir=in action=allow protocol=tcp localport=3389").read()
    if "Rule Name" in rdp:
        print("  [!] WARNING: Remote Desktop (port 3389) is open")
    else:
        print("  [OK] Remote Desktop port is closed")

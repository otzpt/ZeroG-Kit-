import secrets
import string
import hashlib
import psutil
import platform
import os
import qrcode
import re
import cryptography
from cryptography.fernet import Fernet
import base64

def passwordgen(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()
def unitconv():
    while True:
        print("")
        print("  +----------------------------------+")
        print("  |       UNIT CONVERTER             |")
        print("  +----------------------------------+")
        print("  |  [1]  Temperature  (C / F / K)  |")
        print("  |  [2]  Weight       (kg / lb / g) |")
        print("  |  [3]  Length       (m / ft / in) |")
        print("  |  [4]  Data size    (KB / MB / GB)|")
        print("  |  [0]  Back to main menu          |")
        print("  +----------------------------------+")
        choice = input("  > choose a category: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print("  Convert from: [1] Celsius  [2] Fahrenheit  [3] Kelvin")
            src = input("  > ").strip()
            val = float(input("  > enter value: "))
            if src == "1":
                print("  -> Fahrenheit: " + str(round(val * 9/5 + 32, 4)))
                print("  -> Kelvin:     " + str(round(val + 273.15, 4)))
            elif src == "2":
                print("  -> Celsius:    " + str(round((val - 32) * 5/9, 4)))
                print("  -> Kelvin:     " + str(round((val - 32) * 5/9 + 273.15, 4)))
            elif src == "3":
                print("  -> Celsius:    " + str(round(val - 273.15, 4)))
                print("  -> Fahrenheit: " + str(round((val - 273.15) * 9/5 + 32, 4)))
            else:
                print("  invalid option")

        elif choice == "2":
            print("  Convert from: [1] Kilograms  [2] Pounds  [3] Grams")
            src = input("  > ").strip()
            val = float(input("  > enter value: "))
            if src == "1":
                print("  -> Pounds: " + str(round(val * 2.20462, 4)))
                print("  -> Grams:  " + str(round(val * 1000, 4)))
            elif src == "2":
                print("  -> Kilograms: " + str(round(val / 2.20462, 4)))
                print("  -> Grams:     " + str(round(val / 2.20462 * 1000, 4)))
            elif src == "3":
                print("  -> Kilograms: " + str(round(val / 1000, 4)))
                print("  -> Pounds:    " + str(round(val / 1000 * 2.20462, 4)))
            else:
                print("  invalid option")

        elif choice == "3":
            print("  Convert from: [1] Meters  [2] Feet  [3] Inches")
            src = input("  > ").strip()
            val = float(input("  > enter value: "))
            if src == "1":
                print("  -> Feet:   " + str(round(val * 3.28084, 4)))
                print("  -> Inches: " + str(round(val * 39.3701, 4)))
            elif src == "2":
                print("  -> Meters: " + str(round(val / 3.28084, 4)))
                print("  -> Inches: " + str(round(val * 12, 4)))
            elif src == "3":
                print("  -> Meters: " + str(round(val / 39.3701, 4)))
                print("  -> Feet:   " + str(round(val / 12, 4)))
            else:
                print("  invalid option")

        elif choice == "4":
            print("  Convert from: [1] Kilobytes  [2] Megabytes  [3] Gigabytes")
            src = input("  > ").strip()
            val = float(input("  > enter value: "))
            if src == "1":
                print("  -> Megabytes:  " + str(round(val / 1024, 6)))
                print("  -> Gigabytes:  " + str(round(val / 1024**2, 6)))
            elif src == "2":
                print("  -> Kilobytes:  " + str(round(val * 1024, 4)))
                print("  -> Gigabytes:  " + str(round(val / 1024, 6)))
            elif src == "3":
                print("  -> Megabytes:  " + str(round(val * 1024, 4)))
                print("  -> Kilobytes:  " + str(round(val * 1024**2, 4)))
            else:
                print("  invalid option")

        else:
            print("  invalid option")

def sysinfo():
    osname = platform.system()
    osver = platform.version()

    ramTotal = round(psutil.virtual_memory().total / 1024**3)
    ramAvail = round(psutil.virtual_memory().available / 1024**3)
    
    cpu = psutil.cpu_percent(interval = 1)

    diskT = round(psutil.disk_usage('/').total / 1024**3, 2)
    diskA = round(psutil.disk_usage('/').free / 1024**3, 2)

    print("\n  -- SYSTEM INFO --")
    print(f"  OS:          {osname} {osver[:22]}")
    print(f"  RAM:         {ramAvail} GB free / {ramTotal} GB total")
    print(f"  CPU:         {cpu}%")
    print(f"  Disk:        {diskA} GB free / {diskT} GB total")

def QRCgen():
    qr = qrcode.QRCode()
    data = input("Write the content of QRcode(URL, e.g., text): ")
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image()
    img.save("qrcode.png")
    print("image was saved succesfully")

def passwordCheck(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*()]', password) is not None
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    if criteria_met == 5:
        return "strong"
    elif criteria_met == 4:
        return "strong"
    elif criteria_met == 3:
        return "medium"
    elif criteria_met == 2:
        return "weak"
    else:
        return "weak"

def vulnChk(file_path):
    code = open(file_path).read()
    issues = []

    if "eval(" in code:
        issues.append("eval() found - can execute arbitrary code")
    if "exec(" in code:
        issues.append("exec() found - ")
    if "os.system(" in code:
        issues.append("os.system() found - ")
    if "subprocess" in code:
        issues.append("subprocess found - ")
    if "pickle.loads(" in code:
        issues.append("pickle.loads found - ")
    if not issues:
        print("no vunerabilities found")
    else:
        for code in issues:
            print(code)

def encrypt():
    while True:
        print("\n  +---------------------------+")
        print("  |     ENCRYPTION TOOL       |")
        print("  +---------------------------+")
        print("  |  [1]  Encrypt text        |")
        print("  |  [2]  Decrypt text        |")
        print("  |  [0]  Back to main menu   |")
        print("  +---------------------------+")
        choice = input("  > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            text = str(input("insert the text you want to encrypt: "))
            key = str(input("insert the key: "))
            key_bytes = hashlib.sha256(key.encode()).digest()
            f_key = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(f_key)
            text = f.encrypt(text.encode())
            print(text.decode())
        elif choice == "2":
            text = str(input("insert the text you want to decrypt: "))
            key = str(input("insert the key: "))
            key_bytes = hashlib.sha256(key.encode()).digest()
            f_key = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(f_key)
            text = f.decrypt(text.encode())
            print(text.decode())
        else:
            print("invalid option")

def firewallChk():
    check = os.popen("netsh advfirewall show allprofiles state").read()
    print(check)

    if "OFF" in check:
        print("WARNING: Firewall is OFF in one or more profiles")
    else:
        print("OK: Firewall is ON in all profiles")

    RemDesk = os.popen("netsh advfirewall firewall show rule dir=in action=allow protocol=tcp localport=3389").read()

    if "Rule Name" in RemDesk:
        print("WARNING: Remote Desktop (port 3389) is open")
    else:
        print("OK: Remote Desktop port is closed")
    
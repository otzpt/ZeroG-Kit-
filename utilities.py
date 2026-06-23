import secrets
import string
import hashlib
import psutil
import platform

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


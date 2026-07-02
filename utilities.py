import os
import secrets
import string
import psutil
import platform
import qrcode
from PIL import Image


def sysinfo():
    osname = platform.system()
    osver = platform.version()
    ramTotal = round(psutil.virtual_memory().total / 1024**3)
    ramAvail = round(psutil.virtual_memory().available / 1024**3)
    cpu = psutil.cpu_percent(interval=1)
    diskT = round(psutil.disk_usage('/').total / 1024**3, 2)
    diskA = round(psutil.disk_usage('/').free / 1024**3, 2)

    print("\n  -- SYSTEM INFO --")
    print(f"  OS:    {osname} {osver[:22]}")
    print(f"  RAM:   {ramAvail} GB free / {ramTotal} GB total")
    print(f"  CPU:   {cpu}%")
    print(f"  Disk:  {diskA} GB free / {diskT} GB total")


def image_converter():
    img_orig = input("  Image filename (e.g., image.png): ").strip().strip('"')
    img_new = input("  New format (e.g., jpg, bmp): ").strip().lstrip(".").lower()
    if not os.path.isfile(img_orig):
        print("  Error: file not found -> " + img_orig)
        return
    print("  Converting...")
    try:
        with Image.open(img_orig) as img:
            if img_new in ("jpg", "jpeg") and img.mode in ("RGBA", "LA", "P"):
                img = img.convert("RGB")
            base = os.path.splitext(os.path.basename(img_orig))[0]
            out = base + "_converted." + img_new
            img.save(out)
        print("  Done! Saved as " + out)
    except Exception as e:
        print("  Failed: " + str(e))


def QRCgen():
    data = input("  Content (URL, text, etc.): ").strip()
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    qr.make_image().save("qrcode.png")
    print("  Saved as qrcode.png")


def passwordgen(length=16):
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


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
        print("  |  [0]  Back                       |")
        print("  +----------------------------------+")
        choice = input("  > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            print("  [1] Celsius  [2] Fahrenheit  [3] Kelvin")
            src = input("  Convert from: ").strip()
            val = float(input("  Value: "))
            if src == "1":
                print(f"  -> {round(val * 9/5 + 32, 4)} F")
                print(f"  -> {round(val + 273.15, 4)} K")
            elif src == "2":
                print(f"  -> {round((val - 32) * 5/9, 4)} C")
                print(f"  -> {round((val - 32) * 5/9 + 273.15, 4)} K")
            elif src == "3":
                print(f"  -> {round(val - 273.15, 4)} C")
                print(f"  -> {round((val - 273.15) * 9/5 + 32, 4)} F")
            else:
                print("  invalid option")
        elif choice == "2":
            print("  [1] Kilograms  [2] Pounds  [3] Grams")
            src = input("  Convert from: ").strip()
            val = float(input("  Value: "))
            if src == "1":
                print(f"  -> {round(val * 2.20462, 4)} lb")
                print(f"  -> {round(val * 1000, 4)} g")
            elif src == "2":
                print(f"  -> {round(val / 2.20462, 4)} kg")
                print(f"  -> {round(val / 2.20462 * 1000, 4)} g")
            elif src == "3":
                print(f"  -> {round(val / 1000, 4)} kg")
                print(f"  -> {round(val / 1000 * 2.20462, 4)} lb")
            else:
                print("  invalid option")
        elif choice == "3":
            print("  [1] Meters  [2] Feet  [3] Inches")
            src = input("  Convert from: ").strip()
            val = float(input("  Value: "))
            if src == "1":
                print(f"  -> {round(val * 3.28084, 4)} ft")
                print(f"  -> {round(val * 39.3701, 4)} in")
            elif src == "2":
                print(f"  -> {round(val / 3.28084, 4)} m")
                print(f"  -> {round(val * 12, 4)} in")
            elif src == "3":
                print(f"  -> {round(val / 39.3701, 4)} m")
                print(f"  -> {round(val / 12, 4)} ft")
            else:
                print("  invalid option")
        elif choice == "4":
            print("  [1] Kilobytes  [2] Megabytes  [3] Gigabytes")
            src = input("  Convert from: ").strip()
            val = float(input("  Value: "))
            if src == "1":
                print(f"  -> {round(val / 1024, 6)} MB")
                print(f"  -> {round(val / 1024**2, 6)} GB")
            elif src == "2":
                print(f"  -> {round(val * 1024, 4)} KB")
                print(f"  -> {round(val / 1024, 6)} GB")
            elif src == "3":
                print(f"  -> {round(val * 1024, 4)} MB")
                print(f"  -> {round(val * 1024**2, 4)} KB")
            else:
                print("  invalid option")
        else:
            print("  invalid option")

def processK():
    process_list = [p.info for p in psutil.process_iter(['pid', 'name', 'memory_percent'])]
    process_list_ordenada = sorted(process_list, key=lambda x: x['memory_percent'], reverse=True)
    for p in process_list_ordenada[:30]:
        print(f"{p['pid']:8} {p['name']:20} {p['memory_percent']:5.1f}%")

def kill_process(name):
    killed = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == name.lower():
            try:
                psutil.Process(proc.info['pid']).terminate()
                killed.append(proc.info['pid'])
            except psutil.NoSuchProcess:
                pass
            except psutil.AccessDenied:
                print(f"  Access denied for PID {proc.info['pid']}")
    if killed:
        print(f"  Killed PIDs: {killed}")
    else:
        print("  No matching process found")

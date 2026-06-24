import os
import qrcode
import datetime
from utilities import passwordgen, hash_text, unitconv, sysinfo, QRCgen, passwordCheck, vulnChk, encrypt, firewallChk

from PIL import Image

def clear():
    os.system('cls')

def pause():
    input("\n  press Enter to go back...")
    clear()

while True:
    clear()
    print("+" + "-" * 40 + "+")
    print("|" + "Z E R O G - K I T".center(40) + "|")
    print("|" + "your pocket toolbox".center(40) + "|")
    print("+" + "-" * 40 + "+")
    print("|" + " " * 40 + "|")
    print("|  SYSTEM" + " " * 32 + "|")
    print("|   [1]  Clean Temp & Prefetch files".ljust(41) + "|")
    print("|   [2]  View clipboard history".ljust(41) + "|")
    print("|   [3]  Image converter".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("|  UTILITIES" + " " * 29 + "|")
    print("|   [4]  Password generator".ljust(41) + "|")
    print("|   [5]  Hash / checksum a string".ljust(41) + "|")
    print("|   [6]  Unit converter".ljust(41) + "|")
    print("|   [7]  QR code Generator".ljust(41) + "|")
    print("|   [8]  View current date and time".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("|   [9]  System info".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("|  SECURITY" + " " * 30 + "|")
    print("|   [10] Password strenght test".ljust(41)+ "|")
    print("|   [11] Python code vunerabilities check".ljust(41)+ "|")
    print("|   [12] Encrypting".ljust(41)+ "|")
    print("|   [13] FireWall config assistent".ljust(41)+ "|")
    print("|" + " " * 40 + "|")
    print("|   [0]  Exit ZeroG".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("+" + "-" * 40 + "+")
    opcao = input(" > choose an option: ")

    if opcao == "1":
        clear()
        print("Cleaning Temp files...")
        os.system('del /q /f /s %TEMP%\*')
        print("Cleaning even more temp files...")
        os.system('del /q /f /s C:\\Windows\\Temp\\*')
        print("Cleaning Prefetch...")
        os.system('del /q /f /s C:\\Windows\\Prefetch\\*')
        print("\nDone! All temp files cleared.")
        pause()
    elif opcao == "2":
        clear()
        print("  -- CLIPBOARD HISTORY --\n")
        os.system('powershell Get-Clipboard')
        pause()
    elif opcao == "3":
        clear()
        img_orig = input("Enter the image filename (e.g., image.png): ").strip().strip('"')
        img_new = input("Enter the new format extension (e.g., jpg, bmp): ").strip().lstrip('.').lower()
        if not os.path.isfile(img_orig):
            print("Error: file not found -> " + img_orig)
        else:
            print("Converting " + img_orig + "...")
            try:
                with Image.open(img_orig) as img:
                    if img_new in ("jpg", "jpeg") and img.mode in ("RGBA", "LA", "P"):
                        img = img.convert("RGB")
                    base = os.path.splitext(os.path.basename(img_orig))[0]
                    out_name = base + "_converted." + img_new
                    img.save(out_name)
                print("Done! Saved as " + out_name)
            except Exception as e:
                print("Conversion failed: " + str(e))
        pause()
    elif opcao == "4":
        clear()
        length_input = input("Password length (press Enter for 16): ").strip()
        length = int(length_input) if length_input.isdigit() else 16
        print("Generated password: " + passwordgen(length))
        pause()
    elif opcao == "5":
        clear()
        text = input("Enter text to hash: ")
        print("SHA-256: " + hash_text(text))
        pause()
    elif opcao == "6":
        clear()
        unitconv()
        pause()
    elif opcao == "7":
        clear()
        QRCgen()
        pause()
    elif opcao == "8":
        clear()
        now = datetime.datetime.now()
        print("Current date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))
        pause()
    elif opcao == "9":
        clear()
        sysinfo()
        pause()
    elif opcao == "10":
        clear()
        password = input("Enter a password to check: ")
        strenght = passwordCheck(password)
        print(f"Password streght: {strenght}")
        pause()
    elif opcao == "11":
        clear()
        file_path = input("Write the python file path: ").strip()
        vulnChk(file_path)
        pause()
    elif opcao == "12":
        clear()
        encrypt()
        pause()
    elif opcao == "13":
        clear()
        firewallChk()
        pause()
    elif opcao == "0":
        clear()
        print("Goodbye")
        break
    else:
        print("  invalid option")
        pause()

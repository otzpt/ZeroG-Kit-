import os
from utilities import passwordgen, hash_text, unitconv, sysinfo

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
    print("|" + " " * 40 + "|")
    print("|   [7]  System info".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("|   [0]  Exit ZeroG".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("+" + "-" * 40 + "+")
    opcao = input(" > choose an option: ")

    if opcao == "1":
        clear()
        print("Cleaning Temp files...")
        os.system('del /q /f /s %TEMP%\\*')
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
        img_new = input("Enter the new format extension (e.g., jpg, bmp): ").strip().lstrip(".").lower()
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
        sysinfo()
        pause()
    elif opcao == "0":
        clear()
        print("Goodbye")
        break
    else:
        print("  invalid option")
        pause()

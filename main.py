import os
import ctypes
import sys
import datetime

from utilities import sysinfo, image_converter, QRCgen, passwordgen, unitconv
from security import hash_text, passwordCheck, vulnChk, encrypt, firewallChk
from network import networktools
from text_tools import base64_tool, json_formatter, textCaseConv, regex_tester

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()


def clear():
    os.system('cls')


def pause():
    input("\n  press Enter to go back...")
    clear()


def header(title):
    print("+" + "-" * 40 + "+")
    print("|" + title.center(40) + "|")
    print("+" + "-" * 40 + "+")


def system_menu():
    while True:
        clear()
        header("SYSTEM TOOLS")
        print("|   [1]  Clean Temp & Prefetch".ljust(41) + "|")
        print("|   [2]  View Clipboard".ljust(41) + "|")
        print("|   [3]  System Info".ljust(41) + "|")
        print("|   [0]  Back".ljust(41) + "|")
        print("+" + "-" * 40 + "+")
        choice = input(" > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            clear()
            print("  Cleaning Temp files...")
            os.system('del /q /f /s %TEMP%\\*')
            print("  Cleaning Windows Temp...")
            os.system('del /q /f /s C:\\Windows\\Temp\\*')
            print("  Cleaning Prefetch...")
            os.system('del /q /f /s C:\\Windows\\Prefetch\\*')
            print("\n  Done!")
            pause()
        elif choice == "2":
            clear()
            print("  -- CLIPBOARD --\n")
            os.system('powershell Get-Clipboard')
            pause()
        elif choice == "3":
            clear()
            sysinfo()
            pause()
        else:
            print("  invalid option")
            pause()


def utilities_menu():
    while True:
        clear()
        header("UTILITIES")
        print("|   [1]  Image Converter".ljust(41) + "|")
        print("|   [2]  QR Code Generator".ljust(41) + "|")
        print("|   [3]  Unit Converter".ljust(41) + "|")
        print("|   [4]  Password Generator".ljust(41) + "|")
        print("|   [5]  Date & Time".ljust(41) + "|")
        print("|   [0]  Back".ljust(41) + "|")
        print("+" + "-" * 40 + "+")
        choice = input(" > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            clear()
            image_converter()
            pause()
        elif choice == "2":
            clear()
            QRCgen()
            pause()
        elif choice == "3":
            clear()
            unitconv()
        elif choice == "4":
            clear()
            length_input = input("  Password length (Enter for 16): ").strip()
            length = int(length_input) if length_input.isdigit() else 16
            print("  Generated: " + passwordgen(length))
            pause()
        elif choice == "5":
            clear()
            now = datetime.datetime.now()
            print("  Date:  " + now.strftime("%Y-%m-%d"))
            print("  Time:  " + now.strftime("%H:%M:%S"))
            pause()
        else:
            print("  invalid option")
            pause()


def security_menu():
    while True:
        clear()
        header("SECURITY")
        print("|   [1]  Password Strength Check".ljust(41) + "|")
        print("|   [2]  Hash / SHA-256".ljust(41) + "|")
        print("|   [3]  Encrypt / Decrypt".ljust(41) + "|")
        print("|   [4]  Python Vuln. Check".ljust(41) + "|")
        print("|   [5]  Firewall Check".ljust(41) + "|")
        print("|   [0]  Back".ljust(41) + "|")
        print("+" + "-" * 40 + "+")
        choice = input(" > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            clear()
            password = input("  Password to check: ")
            print("  Strength: " + passwordCheck(password))
            pause()
        elif choice == "2":
            clear()
            text = input("  Text to hash: ")
            print("  SHA-256: " + hash_text(text))
            pause()
        elif choice == "3":
            clear()
            encrypt()
        elif choice == "4":
            clear()
            file_path = input("  Python file path: ").strip().strip('"')
            vulnChk(file_path)
            pause()
        elif choice == "5":
            clear()
            firewallChk()
            pause()
        else:
            print("  invalid option")
            pause()


def text_menu():
    while True:
        clear()
        header("TEXT & DATA")
        print("|   [1]  Base64 Tool".ljust(41) + "|")
        print("|   [2]  JSON Formatter".ljust(41) + "|")
        print("|   [3]  Case Converter".ljust(41) + "|")
        print("|   [4]  Regex Tester".ljust(41) + "|")
        print("|   [0]  Back".ljust(41) + "|")
        print("+" + "-" * 40 + "+")
        choice = input(" > ").strip()

        if choice == "0":
            break
        elif choice == "1":
            clear()
            base64_tool()
        elif choice == "2":
            clear()
            json_formatter()
            pause()
        elif choice == "3":
            clear()
            textCaseConv()
        elif choice == "4":
            clear()
            regex_tester()
            pause()
        else:
            print("  invalid option")
            pause()


while True:
    clear()
    print("+" + "-" * 40 + "+")
    print("|" + "Z E R O G - K I T".center(40) + "|")
    print("|" + "your pocket toolbox".center(40) + "|")
    print("+" + "-" * 40 + "+")
    print("|" + " " * 40 + "|")
    print("|   [1]  System Tools".ljust(41) + "|")
    print("|   [2]  Utilities".ljust(41) + "|")
    print("|   [3]  Security".ljust(41) + "|")
    print("|   [4]  Network".ljust(41) + "|")
    print("|   [5]  Text & Data".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("|   [0]  Exit ZeroG".ljust(41) + "|")
    print("|" + " " * 40 + "|")
    print("+" + "-" * 40 + "+")
    opcao = input(" > choose a category: ").strip()

    if opcao == "1":
        system_menu()
    elif opcao == "2":
        utilities_menu()
    elif opcao == "3":
        security_menu()
    elif opcao == "4":
        clear()
        networktools()
    elif opcao == "5":
        text_menu()
    elif opcao == "0":
        clear()
        print("  Goodbye")
        break
    else:
        print("  invalid option")
        pause()

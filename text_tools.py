import re
import base64
import json
import random

def base64_tool():
    while True:
        print("")
        print("  +---------------------------+")
        print("  |       BASE64 TOOL         |")
        print("  +---------------------------+")
        print("  |  [1]  Encode              |")
        print("  |  [2]  Decode              |")
        print("  |  [0]  Back                |")
        print("  +---------------------------+")
        option = input("  > ").strip()

        if option == "0":
            break
        elif option == "1":
            text = input("  Text to encode: ")
            print("  Encoded: " + base64.b64encode(text.encode()).decode())
            input("  press Enter to continue...")
        elif option == "2":
            text = input("  Text to decode: ")
            try:
                print("  Decoded: " + base64.b64decode(text).decode())
            except Exception:
                print("  Error: invalid base64")
            input("  press Enter to continue...")
        else:
            print("  invalid option")


def json_formatter():
    file = input("  File path: ").strip().strip('"')
    try:
        with open(file) as f:
            print(json.dumps(json.load(f), indent=4))
    except FileNotFoundError:
        print("  Error: file not found")
    except json.JSONDecodeError:
        print("  Error: invalid JSON")


def textCaseConv():
    while True:
        print("")
        print("  +--------------------+")
        print("  |   CASE CONVERTER   |")
        print("  +--------------------+")
        print("  | [1]  UPPER CASE    |")
        print("  | [2]  lower case    |")
        print("  | [3]  Title Case    |")
        print("  | [4]  camelCase     |")
        print("  | [5]  snake_case    |")
        print("  | [0]  Back          |")
        print("  +--------------------+")
        option = input("  > ").strip()

        if option == "0":
            break
        elif option in ("1", "2", "3", "4", "5"):
            text = input("  Text: ")
            if option == "1":
                print("  " + text.upper())
            elif option == "2":
                print("  " + text.lower())
            elif option == "3":
                print("  " + text.title())
            elif option == "4":
                words = text.split()
                if words:
                    print("  " + words[0].lower() + "".join(w.capitalize() for w in words[1:]))
            elif option == "5":
                print("  " + "_".join(text.split()).lower())
            input("  press Enter to continue...")
        else:
            print("  invalid option")


def regex_tester():
    pattern = input("  Regex pattern: ")
    text = input("  Text: ")
    try:
        result = re.findall(pattern, text)
        print("  Matches: " + str(result) if result else "  No matches found")
    except re.error:
        print("  Error: invalid regex")

def LIG():
    Ipsum = [
        "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", 
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", 
        "magna", "aliqua", "Ut", "enim", "ad", "minim", "veniam", "quis", "nostrud", 
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", 
        "commodo", "consequat", "Duis", "aute", "irure", "dolor", "in", "reprehenderit", 
        "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", 
        "pariatur", "Excepteur", "sint", "occaecat", "cupidatat", "non", "proident", 
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", 
        "est", "laborum"
    ]
    
    palavras = int(input("Write the amount of words you want to generate: "))

    generated = 0

    generated = random.choices(Ipsum, k = palavras)

    generated = " ".join(generated)

    print(generated)

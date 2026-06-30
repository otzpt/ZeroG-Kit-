import os
import socket


def networktools():
    while True:
        print("")
        print("  +----------------------------------+")
        print("  |         NETWORK TOOLS            |")
        print("  +----------------------------------+")
        print("  |  [1]  Ping host                  |")
        print("  |  [2]  Local / Public IP          |")
        print("  |  [3]  Check if port is open      |")
        print("  |  [4]  Scan active IPs            |")
        print("  |  [0]  Back                       |")
        print("  +----------------------------------+")
        option = input("  > ").strip()

        if option == "0":
            break
        elif option == "1":
            host = input("  Host: ")
            os.system("ping -n 4 " + host)
            input("  press Enter to continue...")
        elif option == "2":
            local = socket.gethostbyname(socket.gethostname())
            print(f"  Local IP:  {local}")
            public = os.popen("curl -s ifconfig.me").read().strip()
            print(f"  Public IP: {public}")
            input("  press Enter to continue...")
        elif option == "3":
            host = input("  Host: ")
            port = int(input("  Port: "))
            try:
                socket.create_connection((host, port), timeout=3)
                print(f"  Port {port} is OPEN on {host}")
            except:
                print(f"  Port {port} is CLOSED on {host}")
            input("  press Enter to continue...")
        elif option == "4":
            local = socket.gethostbyname(socket.gethostname())
            prefix = local.rsplit(".", 1)[0]
            active = []
            print("  Scanning network, please wait (this may take a few minutes)...")
            for i in range(1, 256):
                ip = prefix + "." + str(i)
                if "Reply from" in os.popen("ping -n 1 -w 100 " + ip).read():
                    active.append(ip)
            print("\n  Active IPs:")
            for ip in active:
                print("    " + ip)
            input("  press Enter to continue...")
        else:
            print("  invalid option")

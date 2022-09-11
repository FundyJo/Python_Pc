import socket
import sys
from datetime import datetime

print("##########################")
print("#                        #")
print("#     By Trollagent      #")
print("#                        #")
print("##########################")
print("")

while True:
    targetDomain = input("Enter Domain or IP: ")
    try:
        targetIP = socket.gethostbyname(targetDomain)
        break
    except Exception:
        print(f'"{targetDomain}" is not a valid Domain')

print(targetIP)

openports = []

tstart = datetime.now()

while True:
    minport = input("Min. Port: ")
    maxport = input("Max. Port: ")
    try:
        minport = int(minport)
        try:
            maxport = int(maxport)
            if minport > maxport:
                temp = minport
                minport = maxport
                maxport = temp
            break
        except Exception:
            print("Max. Port ist keine Zahl")
    except Exception:
        print("Min. Port ist keine Zahl!")

try:
    for port in range(minport, maxport + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, port))
        if res == 0:
            try:
                print(f"Port {port} is open with type: '{socket.getservbyport(port)}'")
                openports.append(f"{port}:{socket.getservbyport(port)}")
            except Exception:
                print(f"Port {port} is open with type: 'NotFound'")
                openports.append(f"{port}:NotFound")
        else:
            print(f"Port {port} is closed")
        sock.close()

except Exception:
    print("ERROR")
    sys.exit()

tend = datetime.now()
diff = tend - tstart

print(f"Scan completed in {diff}")
print(f"Here is every open port: {openports}")
input("Press Enter to exit")

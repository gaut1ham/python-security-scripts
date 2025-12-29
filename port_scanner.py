import socket

target = input("Enter target IP or domain: ")
ports = [21, 22, 23, 80, 443, 8080]

print(f"\nScanning {target}...\n")

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except socket.error:
        print("Connection error")

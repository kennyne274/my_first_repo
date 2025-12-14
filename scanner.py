# ⚠️ Disclaimer
#This tool is intended for educational and learning purposes only.

#Do NOT use this scanner on networks or systems that you do not own
#or have explicit permission to test.

#Unauthorized port scanning may be illegal or violate acceptable use policies.
#The author is not responsible for any misuse of this code.

import socket
import time

# ===== Target host to scan =====
target = "scanme.nmap.org"
print(f"[+] Starting scan on {target}...\n")

start_time = time.time()

# List to store open ports
open_ports = []

try:
    # Scan ports from 1 to 1024
    for port in range(1, 1025):
        try:
            # Create a TCP socket (IPv4 + TCP)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          
            sock.settimeout(1)
          
            result = sock.connect_ex((target, port))

            # If connection is successful, the port is open
            if result == 0:
                print(f"Port {port:5} → OPEN")
                open_ports.append(port)

        # If the hostname cannot be resolved (DNS error)
        except socket.gaierror:
            print("[!] Unable to resolve host name.")
            break
          
        finally:
            sock.close()

        # ===== Show scan progress =====
        # Display progress every 300 ports
        if port % 300 == 0:
            print(f"    ... scanned up to port {port}")
          
except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user.")

end_time = time.time()

# Calculate total scan duration
scan_time = end_time - start_time

# ===== Display scan results =====
print("\n===== Scan Results =====")

if open_ports:
    print(f"Open ports: {open_ports}")
    print(f"Total open ports: {len(open_ports)}")
else:
    print("Open ports: None (possible firewall blocking)")

print(f"Total scan time: {scan_time:.2f} seconds")
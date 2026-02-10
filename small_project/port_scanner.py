# Simple port scanner created for learning purposes.
# Use it ONLY on your own computer or servers you have explicit permission to scan.
# Unauthorized port scanning is illegal.

import socket
import threading
from time import time

def scan_port(target, port):
    """
    Checks if a specific port on the target IP is open.
    Uses TCP connect method to determine port status.
    """
    try:
        # IPv4(AF_INET) + TCP(SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(1) 
        
        # Try to connect to target IP:port
        # Returns 0 if connection succeeds (port is open)
        result = s.connect_ex((target, port)) 
        if result == 0:
            print(f"[OPEN] Port {port}")

        s.close()
    # Exception handling
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        return
    except socket.gaierror:
        print ('Hostname could not be resolved.')
        return
    except socket.error:
        print ("Couldn't connect to server")
        return 
    

def thread_scan(target, start_port, end_port, thread_count=100):
    """
    Scans multiple ports concurrently using threads.
    Limits the number of simultaneous threads to prevent overload.
    """
    threads = [] 
   
    for port in range(start_port, end_port + 1):
        
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

        # When the number of active threads reaches the limit (thread_count),
        # wait for all of them to finish before creating more
        if len(threads) >= thread_count:
            for t in threads:
                t.join()
            threads = [] # Reset thread list
  
    # Wait for any remaining threads to complete
    for t in threads:
        t.join()


   
def main():

    target = "45.33.32.156" # Test server IP provided by nmap.org
    start_port = 1
    end_port = 1024

    print(f"\nScanning {target} ...\n")
    t1 = time() # 

    thread_scan(target, start_port, end_port)

    t2 = time() # Start time
    total = t2 - t1 # End time
    print("\nScan completed.")
    print(f"Time taken : {round(total, 2)}seconds")

if __name__ == "__main__":
    main()

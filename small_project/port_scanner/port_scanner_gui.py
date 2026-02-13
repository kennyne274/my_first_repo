#  Port Scanner GUI

import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from concurrent.futures import ThreadPoolExecutor
from time import time


class PortScannerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner - Advanced")
        self.root.geometry("720x500")
        self.root.configure(bg="black")

        # input(Target ip, Start Port, End Port)
        input_frame = tk.Frame(root, bg="black")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Target IP:", fg="#71FA1C", bg="black").grid(row=0, column=0)
        self.ip_entry = tk.Entry(input_frame, width=15)
        self.ip_entry.insert(0, "45.33.32.156")
        self.ip_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Start Port:", fg="#71FA1C", bg="black").grid(row=0, column=2)
        self.start_entry = tk.Entry(input_frame, width=6)
        self.start_entry.insert(0, "1")
        self.start_entry.grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="End Port:", fg="#71FA1C", bg="black").grid(row=0, column=4)
        self.end_entry = tk.Entry(input_frame, width=6)
        self.end_entry.insert(0, "1024")
        self.end_entry.grid(row=0, column=5, padx=5)

        # output
        self.result_label = tk.Label(
            root,
            text="READY",
            bg="black",
            fg="cyan",
            font=("Courier", 15, "bold"),
            justify="left",
            anchor="nw",
            width=85,
            height=12
        )
        self.result_label.pack(pady=30, padx=30)

       
        # Progressbar
        self.progress = ttk.Progressbar(
            root,
            orient="horizontal",
            length=650,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        # button
        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Scan Start", width=15, pady=5, command=self.start_scan).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Stop", width=15, pady=5,command=self.stop_scan).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Save Result", width=15, pady=5, command=self.save_result).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Reset", width=15, pady=5, command=self.reset).grid(row=0, column=3, padx=5)

       
        self.open_ports = []
        self.scanned_ports = 0
        self.total_ports = 0
        self.executor = None
        self.stop_event = threading.Event()

    # port scan
    def scan_port(self, target, port):

        if self.stop_event.is_set():
            return

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            s.close()

            if result == 0:
                self.open_ports.append(port)

        except:
            pass

        self.scanned_ports += 1
        self.root.after(0, self.update_progress)

   
    def update_progress(self):

        self.progress["value"] = self.scanned_ports

        percent = int((self.scanned_ports / self.total_ports) * 100)

        self.result_label.config(
            text=f"Scanning...\n"
                 f"Progress: {percent}%\n"
                 f"Open Ports: {self.open_ports}"
        )

    # start scan
    def start_scan(self):

        target = self.ip_entry.get()

        try:
            socket.inet_aton(target)
        except:
            messagebox.showerror("Error", "Invalid IP address")
            return

        try:
            start_port = int(self.start_entry.get())
            end_port = int(self.end_entry.get())
        except:
            messagebox.showerror("Error", "Invalid port range")
            return

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            messagebox.showerror("Error", "Invalid port range")
            return

        
        self.open_ports = []
        self.scanned_ports = 0
        self.total_ports = end_port - start_port + 1
        self.progress["maximum"] = self.total_ports
        self.progress["value"] = 0
        self.stop_event.clear()

        self.executor = ThreadPoolExecutor(max_workers=100)

        def run_scan():
            t1 = time()

            for port in range(start_port, end_port + 1):
                if self.stop_event.is_set():
                    break
                self.executor.submit(self.scan_port, target, port)

            self.executor.shutdown(wait=True)

            t2 = time()
            total = round(t2 - t1, 2)

            if self.stop_event.is_set():
                status = "Scan Stopped!"
            else:
                status = "Scan Completed!"

            self.root.after(0, lambda: self.result_label.config(
                text=f"{status}\n"
                     f"Target: {target}\n"
                     f"Open Ports: {self.open_ports}\n"
                     f"Time: {total} sec"
            ))

        threading.Thread(target=run_scan, daemon=True).start()

    # stop
    def stop_scan(self):
        self.stop_event.set()
        if self.executor:
            self.executor.shutdown(wait=False)
        self.result_label.config(text="Stopping...")

    # save result
    def save_result(self):

        if not self.open_ports:
            messagebox.showinfo("Info", "No open ports found.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        if file_path:
            with open(file_path, "w") as f:
                for port in self.open_ports:
                    f.write(f"{port}\n")

            messagebox.showinfo("Saved", "Result saved successfully.")

    # reset
    def reset(self):
        self.stop_event.set()
        self.open_ports = []
        self.scanned_ports = 0
        self.progress["value"] = 0
        self.result_label.config(text="READY")


# main
if __name__ == "__main__":
    root = tk.Tk()
    app = PortScannerGUI(root)
    root.mainloop()

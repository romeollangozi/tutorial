#!/usr/bin/python3

import socket
import json

HOST = "127.0.0.1"
PORT = 65520

def start_server():
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
          sck.bind((HOST, PORT))
          sck.listen()
          conn, addr = sck.accept()
          while True:
               data = conn.recv(1024)
               if not data:
                    break
               print(f"Recieved dictionary from client:\n{data.decode('ascii')}")

def send_data(data):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
          sck.connect((HOST, PORT))
          sck.sendall(bytes(json.dumps(data), encoding='ascii'))

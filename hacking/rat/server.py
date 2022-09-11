import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_pc = ""
port = 6969

sock.bind((local_pc, port))
sock.listen()

while True:
    print("Server Listening")
    connection, address = sock.accept()
    print(f"Connection to {address}")

    try:
        while True:
            command = input("Command: ")
            connection.sendall(command.encode())
    except:
        print(f"Disconnected from {address}")

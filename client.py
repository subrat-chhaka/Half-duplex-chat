import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
s.connect((host, port))

while (True):
    data = s.recv(1024).decode()
    print("Server : "+ data)
    str = input("  --> ")
    s.send(str.encode())

s.close()
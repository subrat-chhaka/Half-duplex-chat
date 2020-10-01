import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9014
s.connect((host, port))

while (True):
    data1 = s.recv(1024).decode()
    print("Server : "+ data1)
    str = input("  --> ")
    s.send(str.encode())

s.close()
//client file purposed

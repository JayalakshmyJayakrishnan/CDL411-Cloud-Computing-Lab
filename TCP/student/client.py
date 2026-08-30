import socket

host = '127.0.0.1'
port = 12908

client_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_obj.connect((host, port))

book = input("Enter book title: ")

client_obj.send(book.encode())

reply = client_obj.recv(1024).decode()

print("Server:", reply)

client_obj.close()

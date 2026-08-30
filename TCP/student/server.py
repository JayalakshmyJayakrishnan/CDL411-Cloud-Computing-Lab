import socket

host = '127.0.0.1'
port = 12908

books = {
    "python": "Available",
    "java": "Not Available",
    "computer networks": "Available",
    "dbms": "Available"
}

server_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_obj.bind((host, port))
server_obj.listen(1)

print(f"Server listening on {host} : {port}")

conn, addr = server_obj.accept()

book = conn.recv(1024).decode().lower()

if book in books:
    reply = books[book]
else:
    reply = "Book not found"

conn.send(reply.encode())

conn.close()
server_obj.close()

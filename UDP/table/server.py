import socket

host = '127.0.0.1'
port = 12908

tables = {
    1: "Available",
    2: "Occupied",
    3: "Available",
    4: "Occupied",
    5: "Available"
}

server_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_obj.bind((host, port))

print(f"Server listening on {host} : {port}")

while True:
    message, addr = server_obj.recvfrom(1024)
    table_no = int(message.decode())

    if table_no in tables:
        reply = tables[table_no]
    else:
        reply = "Table does not exist."

    server_obj.sendto(reply.encode(), addr)

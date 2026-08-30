import socket

host = '127.0.0.1'
port = 12908

client_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

table_no = input("Enter table number: ")

client_obj.sendto(table_no.encode(), (host, port))

reply, addr = client_obj.recvfrom(1024)
reply = reply.decode()

print("Server:", reply)

client_obj.close()

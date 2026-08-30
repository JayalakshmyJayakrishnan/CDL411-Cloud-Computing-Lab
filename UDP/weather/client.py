import socket

host = '127.0.0.1'
port = 12908

client_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

city = input("Enter city: ")

client_obj.sendto(city.encode(), (host, port))

reply, addr = client_obj.recvfrom(1024)
reply = reply.decode()

print("Server:", reply)

client_obj.close()

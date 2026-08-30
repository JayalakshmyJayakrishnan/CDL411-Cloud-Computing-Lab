import socket

host = '127.0.0.1'
port = 12908

client_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

message = num1 + " " + num2 + " " + operation

client_obj.sendto(message.encode(), (host, port))

reply, addr = client_obj.recvfrom(1024)
reply = reply.decode()

print("Result:", reply)

client_obj.close()

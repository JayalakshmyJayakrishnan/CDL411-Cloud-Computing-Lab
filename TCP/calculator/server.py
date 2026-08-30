import socket

host = '127.0.0.1'
port = 12908

server_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_obj.bind((host, port))
server_obj.listen(1)

print(f"Server listening on {host} : {port}")

conn, addr = server_obj.accept()

message = conn.recv(1024)
message = message.decode()

num1, num2, operation = message.split()

num1 = float(num1)
num2 = float(num2)

if operation == '+':
    reply = num1 + num2
elif operation == '-':
    reply = num1 - num2
elif operation == '*':
    reply = num1 * num2
elif operation == '/':
    reply = num1 / num2
else:
    reply = "Invalid operation"

conn.send(str(reply).encode())

conn.close()
server_obj.close()

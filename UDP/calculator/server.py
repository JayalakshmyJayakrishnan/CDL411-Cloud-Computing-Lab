import socket

host = '127.0.0.1'
port = 12908

server_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_obj.bind((host, port))

print(f"Server listening on {host} : {port}")

while True:
    message, addr = server_obj.recvfrom(1024)
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

    server_obj.sendto(str(reply).encode(), addr)

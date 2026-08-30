import socket

host = '127.0.0.1'
port = 12908

weather = {
    "kochi": "Rainy, 28 C",
    "delhi": "Sunny, 35 C",
    "mumbai": "Cloudy, 30 C",
    "bangalore": "Pleasant, 25 C"
}

server_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_obj.bind((host, port))

print(f"Server listening on {host} : {port}")

while True:
    message, addr = server_obj.recvfrom(1024)
    message = message.decode().lower()

    if message in weather:
        reply = weather[message]
    else:
        reply = "Weather information not available."

    server_obj.sendto(reply.encode(), addr)

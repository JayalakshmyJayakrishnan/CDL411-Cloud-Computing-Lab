import socket
import threading

def handle_client(client_socket, client_address):
	print(f"New connection: {client_address}")
	
	while True:
		try:
			message = client_socket.recv(1024).decode('utf-8')
			if not message or message.lower()=='exit':
				print("Client has terminated the connection.")
				break
			print(f"{client_address}:{message}")
			broadcast(f"{client_address}:{message}",client_socket)
		except:
			break
	client_socket.close()
	
def broadcast(message, sender_socket):
	for client in clients:
		if client!=sender_socket:
			try:
				client.send(message.encode('utf-8'))
			except:
				client.close()
				clients.remove(client)

server_ip = '127.0.0.1'
server_port = 3333
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)



clients = []
print(f"Server started on {server_ip}:{server_port}")


while True:
	client_socket, client_address = server.accept()
	clients.append(client_socket)
	threading.Thread(target=handle_client, args = (client_socket, client_address)).start()

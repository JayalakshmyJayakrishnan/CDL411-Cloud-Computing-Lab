import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)

        except:
            print("An error occurred!")
            client_socket.close()
            break


def send_messages():
    while True:
        message = input("> ") #Adding this cz the texts kept disappearing
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            print("Terminating the connection.")
            break


server_ip = '127.0.0.1'
server_port = 3333

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()

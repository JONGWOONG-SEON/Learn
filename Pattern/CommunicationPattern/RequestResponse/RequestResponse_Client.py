import socket
from datetime import datetime

def client_start():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1",4444))
    
    message = "요청 시간: " + str(datetime.now())

    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()

    print(f"{response}")

    client_socket.close()

client_start()
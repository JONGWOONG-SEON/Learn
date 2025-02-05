import socket
import time

def sync_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 4444))
    time.sleep(10)
    client_socket.send(b"Hello, Hi I'm TimeSleep")
    response = client_socket.recv(1024)
    print(f"서버 응답: {response.decode()}")

    client_socket.close()

sync_client()




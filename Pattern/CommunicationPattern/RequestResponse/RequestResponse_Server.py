import socket
from datetime import datetime

total_connect = 0

def server_start():
    global total_connect

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1",4444))
    server_socket.listen(0)
    print("요청 응답 서버가 실행 중")

    while True:
        conn, addr = server_socket.accept()
        print(f"클라이언트 {addr} 연결됨.")

        request = conn.recv(1024).decode()
        print(f"{request} {addr}")

        response = "응답 시간: " + str(datetime.now())

        conn.sendall(response.encode())
        total_connect += 1
        conn.close()
        if total_connect >= 5:
           server_socket.close()
           break

server_start()
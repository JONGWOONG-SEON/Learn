import socket

def sync_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 4444))
    server_socket.listen(0)
    print("동기 서버가 실행 중...")

    total_connection = 0

    while True:
        client_socket, addr = server_socket.accept()
        print(f"클라이언트 {addr} 연결됨")

        data = client_socket.recv(1024)
        print(f"받은 데이터: {data.decode()}")

        response = "서버 응답: " + data.decode()
        client_socket.send(response.encode())

        client_socket.close()  # 동기 방식이므로 한 번에 하나의 클라이언트만 처리
        total_connection += 1
        if total_connection == 2:
            server_socket.close()
            break

sync_server()

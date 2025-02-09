import socket

def push_client_start():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 4444))
    print("서버와 연결 되었습니다.")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(f"서버 푸시 메시지: {message}")
        except:
            print("서버와 연결이 종료되었습니다.")
            break

push_client_start()
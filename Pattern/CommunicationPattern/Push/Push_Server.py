import socket
import time
import threading

class Spec:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 4444
        self.clients = [] # 공유 변수

class Push(Spec):
    def __init__(self, handler):
        super().__init__()
        self.handler = handler
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.ip, self.port))
        self.socket_server.listen(5)
        print("푸시 서버 실행 중...")

    def accept_run(self):
        """클라이언트의 연결을 처리하는 스레드 함수"""
        while True:
            conn, addr = self.socket_server.accept()
            print(f"클라이언트 {addr} 연결됨.")
            self.clients.append(conn)  # 클라이언트 연결 시 리스트에 추가

    def server_run(self):
        """푸시 서버 실행 및 자동 메시지 전송"""
        threading.Thread(target=self.accept_run, daemon=True).start()  # 클라이언트 수락 스레드 실행

        while True:
            time.sleep(5)
            self.handler.push_by_server(self.clients)  # clients 리스트를 handler에 전달

class Push_Handler:

    def push_by_server(self, clients):
        """서버에서 클라이언트에게 자동으로 푸시 메시지를 전송"""
        message = "[Push] \n 서버에서 자동으로 전송하는 메시지"
        print(f"전송: {message}")
        
        # 전달받은 clients 리스트 사용
        for client in clients:
            try:
                client.sendall(message.encode())  # 클라이언트에게 메시지 전송
            except:
                clients.remove(client)  # 연결이 끊긴 클라이언트 제거

if __name__ == "__main__":
    handler = Push_Handler()
    server = Push(handler)
    server.server_run()

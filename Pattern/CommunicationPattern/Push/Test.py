addr = ("127.0.0.1",4444)

print(f"{addr[1]} \ntest")




import socket
import time
import threading

class Spec:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 4444
        self.clients = []
        self.socket_server = None
        # self.conn = None

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
            self.clients.append(conn)
            print(self.clients.append(conn))

    def server_run(self):
        """푸시 서버 실행 및 자동 메시지 전송"""
        threading.Thread(target=self.accept_run, daemon=True).start() 

        while True:
            time.sleep(5)
            self.handler.push_by_server()
            # self.handler.push_by_admin()

class Push_Handler(Spec):
    def __init__(self):
        super().__init__()


    def push_by_server(self):

        message = "[Push] \n서버에서 자동으로 전송하는 메시지"
        print(f"전송: {message}")
        print(self.clients)
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except:
                self.clients.remove(client)


    def push_by_admin(self):
        
        if self.port == 4445:
            messages = "[Push Admin] \n" + str(self.socket_server.recv(1024).decode())
        for client in self.clients:
            try:
                client.sendall(messages.encode())
            except:
                self.clients.remove(client)
    
if __name__ == "__main__":
    handler = Push_Handler()
    server = Push(handler)
    server.server_run()

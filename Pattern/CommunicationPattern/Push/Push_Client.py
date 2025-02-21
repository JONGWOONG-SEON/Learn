import socket
import threading

class Port:
    def __init__(self):
        self._portlist = []
    
    def __iter__(self):
        return PortIterator(self._portlist)

    def get(self,index):
        return self._portlist[index]
    
    def set(self,l):
        self._portlist = l

class PortIterator:
    def __init__(self,port):
        self._portlist = port
        self._size = len(port)
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._size:
            pos = self._index
            self._index += 1
            return self._portlist[pos]
        
        else:
            raise StopIteration()

class Instance:
    def __init__(self):
        self._instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._session = None

class PushClient(Instance):
    def __init__(self):
        super().__init__()
        self._port = None
    
    def connect(self,port : int):
        try:
            self._instance.bind(("127.0.0.1",port))
            self._instance.connect(("127.0.0.1",4445))
            self._session = True
            self._port = port
            print(f"{port} 서버와 연결되었습니다.")
        except Exception as e:
            print(e)

    def start(self):
        while self._session:
            try:
                message = self._instance.recv(1024).decode()
                print(f"[{self._port}] : {message}")
            except:
                print("서버와 연결이 종료되었습니다.")
                break

    def run_in_daemon(self):
        thread = threading.Thread(target=self.start,daemon=True)
        return thread

def main():
    port = Port()
    port.set([4440,4441,4442,4443])
    for port_value in list(port):
        pushclient = PushClient()
        pushclient.connect(port_value)
        thread = pushclient.run_in_daemon()
        thread.start()




# def push_client_start(port):
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(("127.0.0.1", port))
#     print(f"{port}서버와 연결 되었습니다.")
#     while True:
#         try:
#             message = client_socket.recv(1024).decode()
#             print(f"[{port}] : {message}")
#         except:
#             print("서버와 연결이 종료되었습니다.")
#             break


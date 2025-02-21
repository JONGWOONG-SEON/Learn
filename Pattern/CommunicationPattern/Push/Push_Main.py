import Push_Client
import Push_Server
import threading

def run_server():
    Push_Server.main()

threading.Thread(target=run_server, daemon= True).start()
Push_Client.main()
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n Push 시뮬레이션 종료")

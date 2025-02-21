import socket

def push_client_start():
    trigger_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trigger_socket.bind(("127.0.0.1", 4446))
    trigger_socket.connect(("127.0.0.1",4444))
    return trigger_socket

def push_trigger(trigger_socket):
    while True:
        input_message = input("Push 메세지 입력 (q 입력 시 종료): ") 

        if input_message.lower() == "q":
            print("연결 종료")
            trigger_socket.close()
            break

        print(f"전송된 메시지: {input_message}")
        trigger_socket.sendall(input_message.encode()) 

push_trigger(push_client_start())

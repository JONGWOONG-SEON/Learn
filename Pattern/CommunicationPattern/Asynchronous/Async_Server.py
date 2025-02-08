import asyncio

total_connection = 0
server = None

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    global total_connection, server

    addr = writer.get_extra_info('peername')
    print(f"클라이언트 {addr} 연결됨")

    data = await reader.read(1024)
    message = data.decode()
    print(f"받은 데이터: {message}")

    response = "서버 응답: " + message
    writer.write(response.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()

    total_connection += 1
    print(f"현재 연결된 클라이언트 수: {total_connection}")

    if total_connection == 2:
        print("서버 종료 중...")
        server.close()
        await server.wait_closed()
        print("서버가 정상적으로 종료되었습니다.")

async def async_server():
    global server
    server = await asyncio.start_server(handle_client, "127.0.0.1", 4444)
    addr = server.sockets[0].getsockname()
    print(f"비동기 서버가 {addr}에서 실행 중...")

    try:
        async with server:
            await server.serve_forever()
    except asyncio.CancelledError:
        print("서버가 종료되었습니다.") 

if __name__ == "__main__":
    try:
        asyncio.run(async_server())  
    except KeyboardInterrupt:
        print("서버가 강제 종료되었습니다.")

import asyncio

async def async_client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 5001)

    writer.write(b"Hello, Async Server")
    await writer.drain()  # 전송 완료 대기

    response = await reader.read(1024)
    print(f"서버 응답: {response.decode()}")

    writer.close()
    await writer.wait_closed()

asyncio.run(async_client())

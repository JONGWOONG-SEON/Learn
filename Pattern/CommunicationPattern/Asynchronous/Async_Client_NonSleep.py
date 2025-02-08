import asyncio

async def async_client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 4444)
    
    message = "Hello, Hi I'm Non TimeSleep"
    writer.write(message.encode())
    await writer.drain()

    response = await reader.read(1024)
    print(f"{response.decode()}")

    writer.close()
    await writer.wait_closed()

asyncio.run(async_client())

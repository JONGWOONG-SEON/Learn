import asyncio
import time

class Creational:
    def __init__(self):
        self._break = "Response Break Point"

    def call(self):
        print(self._break)

class SyncCall(Creational):
    def __init__(self):
        super().__init__()

    # Synchronous method: blocking call
    def call(self):
        print("Sync Call Starting")
        time.sleep(5)  # Simulates a blocking process
        super().call()  # Calling the parent method
        print("Sync Response Finished")

class AsyncCall(Creational):
    def __init__(self):
        super().__init__()

    # Asynchronous method: non-blocking
    async def call(self):
        print("Async Call Starting")
        await asyncio.sleep(5)  # Simulates non-blocking behavior
        super().call()  # Calling the parent method
        print("Async Response Finished")

# Run the synchronous and asynchronous function separately
async def main():
    print("Running Synchronous Call:")
    sync = SyncCall()
    sync.call()  # This will block the program for 5 seconds before proceeding
    
    print("\nRunning Asynchronous Call:")
    async_call = AsyncCall()
    await async_call.call()  # This will run asynchronously and will not block the program

if __name__ == "__main__":
    asyncio.run(main())  # Ensures the async function is run correctly

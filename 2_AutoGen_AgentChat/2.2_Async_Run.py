import asyncio
import time

async def make_hot_chocolate():
    print("Starting to make Hot Chocolate")
    await asyncio.sleep(3)
    print("Hot Chocolate is ready")

async def toast_bread():
    print("Starting to Toast Bread")
    await asyncio.sleep(2)
    print("Toasted Bread is ready")


async def main():
    start = time.time()

    hot_chocolate = make_hot_chocolate()
    toasted_bread = toast_bread()

    results = await asyncio.gather(hot_chocolate, toasted_bread)

    end = time.time()

    print(f"Time: {end - start:.2f} minutes")

asyncio.run(main())

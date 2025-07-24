import asyncio
import time

async def brew_Hot_Choclate():
    print("Starting Brewing Hot Choclate")
    await asyncio.sleep(3)
    print("Hot Choclate Ready")

async def toast_Toast():
    print("Start Toasting Toast")
    await asyncio.sleep(2)
    print("Toast Ready")


async def main():
    start = time.time()

    coffee = brew_Hot_Choclate()
    toast = toast_Toast()

    results = await asyncio.gather(coffee,toast)

    end = time.time()

    print(f"Time : {end - start:.2f} minutes")


asyncio.run(main())
import asyncio

event = asyncio.Event()


async def waiter():
    print("a")
    await event.wait()
    print("b")

async def main():
    task = asyncio.create_task(waiter())
    print("c")
    event.set()
    await task

asyncio.run(main())

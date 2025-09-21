import asyncio

async def display():
    await asyncio.sleep(1)
    return ("hello world")

async def main():

    tasks = asyncio.gather(display(), display(), display())
    await tasks
    for result in tasks.result():
        print(result)

asyncio.run(main())
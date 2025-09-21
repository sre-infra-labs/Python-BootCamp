import asyncio

class Calculator():
    async def add(self, first, second):
        print("pls wait...")
        await asyncio.sleep(5)
        print("resumed")
        return first+second

    def print(self): pass

async def main():
    calc = Calculator()
    sum = await calc.add(1, 5)
    print("sum: ", sum)

asyncio.run(main())
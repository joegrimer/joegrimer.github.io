import asyncio
import random

superdict = {}
a = 0


async def append():
    global a
    await asyncio.sleep(random.randint(0, 50)/2)
    superdict[a] = 1
    a += 1
    print("added", str(a))


async def main():
    await asyncio.gather(*[append() for _ in range(0, 1000)])

asyncio.run(main())

print("a", a)
print("len sd", str(len(superdict)))





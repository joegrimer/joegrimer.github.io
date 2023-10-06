import asyncio

async def jakub():
    return [1]

async def main():
    await jakub()[0]

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

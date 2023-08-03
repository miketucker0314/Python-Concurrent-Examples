import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def count_test():
    s = time.perf_counter()
    await asyncio.gather(count(), count(), count())
    elapsed = time.perf_counter() - s
    print(f"Count Test executed in {elapsed:0.2f} seconds.")


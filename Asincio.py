import asyncio
import time

 
async def boil_kettle():
    await asyncio.sleep(3)
    print("чай готов")

async def fry_egg():
    await asyncio.sleep(2)
    print("яйца готовы")

async def main():
    start = time.perf_counter()
    await boil_kettle()
    await fry_egg()
    print(f"Время при последовательном: {time.perf_counter() - start:.3f}")


    start1 = time.perf_counter()
    await asyncio.gather(boil_kettle(), fry_egg())
    print(f"Время при одновременном запуске: {time.perf_counter() - start1:.3f}")

asyncio.run(main())
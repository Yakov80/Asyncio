import asyncio
import time

 
async def boil_kettle():
    await asyncio.sleep(3)
    print("чай готов")

async def fry_egg():
    await asyncio.sleep(2)
    print("яйца готовы")
    
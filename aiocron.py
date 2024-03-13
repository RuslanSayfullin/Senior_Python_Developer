import aiocron
import asyncio

@aiocron.crontab('*/30****')
async def hi():
    print('Hello!')

asyncio.get_event_loop().run_forever()

import asyncio
import aiohttp
import time

start = time.time()
session = aiohttp.ClientSession()


async def get(url):
    response = await session.get(url)
    result = response.status
    return result

count = 0

async def request():
    global count
    url = 'https://www.baidu.com'
    print('Waiting for', url)
    result = await get(url)
    count += 1
    print(count)
    print('Get response from', url, 'Result:', result)


tasks = [asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
session.close()

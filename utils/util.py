import aiohttp


async def slow_route(route_url:str):
    async with aiohttp.ClientSession() as session:
        async with session.get(route_url) as resp:
            return await  resp.json()
import asyncio
import time
import aiohttp


async def download_site(session, url, counter):
    print(f"do the request for task {counter}")
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url} for task {counter}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        counter = 0
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url, counter))
            tasks.append(task)
            counter += 1
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

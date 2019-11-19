import asyncio
import random
import sys
import time
import itertools as it
import os


def make_item() -> int:
    return os.urandom(5).hex()


async def rand_sleep(caller=None) -> None:
    i = random.randint(0, 10)
    print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, queue: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):
        await rand_sleep(caller=f"Producer {name}")
        i = make_item()
        t = time.perf_counter()
        await queue.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, queue: asyncio.Queue) -> None:
    while True:
        await rand_sleep(caller=f"Consumer {name}")
        i, t = await queue.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now - t:0.5f} seconds.")
        queue.task_done()


async def main(n_prod: int, n_con: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(n_prod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(n_con)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    print(q.qsize())
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    number_of_producers = int(sys.argv[1])
    number_of_consumers = int(sys.argv[2])
    print(f"The number of producers are {number_of_producers}")
    print(f"The number of consumers are {number_of_consumers}")
    start = time.perf_counter()
    asyncio.run(main(number_of_producers, number_of_consumers))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")

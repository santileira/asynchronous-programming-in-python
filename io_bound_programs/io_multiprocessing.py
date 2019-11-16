import requests
import multiprocessing
import time

session = None


def set_global_session():
    """
    The initializer function parameter is built for just this case.
    There is not a way to pass a return value back from the initializer to the function called by the process download_site(),
    but you can initialize a global session variable to hold the single session for each process.
    Because each process has its own memory space, the global for each one will be different.
    """
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
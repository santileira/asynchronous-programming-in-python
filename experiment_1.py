import queue


def task(name: str, work_queue: queue.Queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
        return

    while not work_queue.empty():
        print(f"Task {name} running")
        count = work_queue.get()
        print(f"Task {name} total: {count}")


def main():
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]

    for t, n, w in tasks:
        t(n, w)


if __name__ == "__main__":
    main()

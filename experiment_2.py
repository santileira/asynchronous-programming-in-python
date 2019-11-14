import queue


def task(name: str, work_queue: queue.Queue):
    while not work_queue.empty():
        print(f"Task {name} running")
        count = work_queue.get()
        total = 0
        for x in range(count):
            total += 1
            yield name
        print(f"Task {name} total: {total}")


def main():
    """
    This method allows to run cooperatively two instances of a task.
    This is still a synchronous program.
    """
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                print("Remove task")
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    main()

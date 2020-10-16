from cloudbutton.multiprocessing import Pool, Lock, SimpleQueue, getpid
import time


def f(lock, q):
    with lock:
        pid = getpid()
        ts = time.time()
        msg = 'process: {} - timestamp: {}'.format(pid, ts)
        q.put(msg)
        time.sleep(1)


if __name__ == "__main__":
    lock = Lock()
    q = SimpleQueue()

    n = 3
    with Pool() as p:
        p.map_async(f, [[lock, q]] * n)

    for _ in range(n):
        print(q.get())
    


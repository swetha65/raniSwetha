import threading
import concurrent.futures
class values:
    def __init__(self, x):
        self.value = x
    def upd(self, name):
        print("Thread {} running".format(name))
        l = threading.Lock()
        l.acquire()
        s = self.value
        s = s + 1
        self.value = s
        l.release()

if __name__ == "__main__":
    t = values(4)
    with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as ex:
        for i in range(3):
            ex.submit(t.upd, i)
    print("final value : {}".format(t.value))
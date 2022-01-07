from multiprocessing import *
import os


def test(a,b):
    print(a+b)
    print(os.getpid())


if __name__ == "__main__":
    p = Process(target=test, args=(2,1))
    t = []
    print(p)
    t.append(p)
    p.start()
    # p.join()

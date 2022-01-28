import time
import timeit


def time_checker():
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s += i

    end_time = time.time()
    return end_time - start_time


n = 10000
print(time_checker())


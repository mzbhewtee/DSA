from memory_profiler import profile


@profile
def time_checker():
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


n = 10000
print(time_checker())

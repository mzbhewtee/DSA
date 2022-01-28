from memory_profiler import profile 
# memory_profiler module for monitoring space consumption 
#This program tracks the memory usage by algorithms

@profile #decorator
#function to monitor space usage
def time_checker():
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


n = 10000
print(time_checker())


import time

# decorator as a function
def time_this(num_runs):
    def wrapper(func):
        avg_time = 0
        for i in range(num_runs):
            print(i)
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)

        avg_time /= num_runs
        print(f"avg_time: {avg_time}")        
        return func
    return wrapper

# decorator as a class
class TimeThis:
    def __init__(self, num_runs):
        self.num_runs = num_runs

    def __call__(self, func):
        avg_time = 0
        for i in range(self.num_runs):
            print(i)
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)

        avg_time /= self.num_runs
        print(f"avg_time: {avg_time}")        
        return func

# @time_this(num_runs=10)
@TimeThis(num_runs=10)
def f():
    for i in range(10_000_000):
        pass

f()

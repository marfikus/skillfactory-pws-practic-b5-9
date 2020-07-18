
import time

def time_this(num_runs):
    def wrapper(func):
        avg_time = 0
        # print(num_runs)
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


@time_this(num_runs=10)
def f():
    # print("f")
    for i in range(10_000_000):
        pass

f()

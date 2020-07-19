"""
Calculating the average execution time of a function
"""
import time

# decorator as a function
def time_this(num_runs):
    def decorator(func):
        def wrapper(*arg, **kwarg):
        # arg & kwarg needed in case if function has parameters
            avg_time = 0
            for i in range(num_runs):
                print(i)
                t0 = time.time()
                func(*arg, **kwarg)
                t1 = time.time()
                avg_time += (t1 - t0)

            avg_time /= num_runs
            print(f"avg_time: {avg_time}")        
            return func
        return wrapper
    return decorator

@time_this(num_runs=10)
def f():
    for i in range(10_000_000):
        pass

f()

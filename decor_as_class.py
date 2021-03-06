"""
Calculating the average execution time of a function
"""
import time

# decorator as a class
class TimeThis:
    def __init__(self, num_runs):
        # num_runs - number of repeats of the function
        self.num_runs = num_runs

    def __call__(self, func):
        def wrapper(*arg, **kwarg):
            # arg & kwarg needed in case if function has parameters
            avg_time = 0
            for i in range(self.num_runs):
                print(i)
                t0 = time.time()
                func(*arg, **kwarg)
                t1 = time.time()
                avg_time += (t1 - t0)

            avg_time /= self.num_runs
            print(f"avg_time: {avg_time}")        
            return func
        return wrapper

@TimeThis(num_runs=10)
def f():
    for i in range(10_000_000):
        pass

f()

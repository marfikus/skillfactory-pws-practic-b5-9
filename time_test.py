
import time

NUM_RUNS = 10
avg_time = 0

for _ in range(NUM_RUNS):
    t0 = time.time()

    for i in range(10000000):
        pass

    t1 = time.time()
    avg_time += (t1 - t0)

avg_time /= NUM_RUNS
print(f"avg_time: {avg_time}")

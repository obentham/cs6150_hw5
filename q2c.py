import math
import random

RUNS = 50
T=[4e4, 9e4, 16e4]

for t in T:
    results = []
    for _ in range(RUNS):
        origin_count=0
        x=0
        for _ in range(int(t)):
            if random.random() > 0.5:
                x += 1
            else:
                x -= 1

            if x == 0:
                origin_count += 1
        results.append(origin_count)

    print(t, sum(results)/RUNS)

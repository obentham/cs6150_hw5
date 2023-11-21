from collections import Counter
import math
import random

N = 1000000
VOTES = [1 if i/N < 0.52 else 0 for i in range(N)]

SAMPLE = [20, 100, 400]
TRIALS = 100

for s in SAMPLE:
    results = []
    for t in range(TRIALS):
        sample = random.sample(VOTES, s)
        #print(sample)
        one_count = sum([1 for v in sample if v == 1])
        #print(one_count)
        results.append(int(one_count > s/2))
        #print(one_count > s/2)
        #print()
    print(s, sum(results)/TRIALS)
    #break

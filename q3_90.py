import argparse
from collections import Counter
import math
import random

import matplotlib.pyplot as plt


N = 1000000
VOTES = [1 if i/N < 0.52 else 0 for i in range(N)]

SAMPLE = [i for i in range(400, 1501, 25)]
TRIALS = 10000


parser = argparse.ArgumentParser()
parser.add_argument('--output', '-o', default='q3_90.png')
args = parser.parse_args()


plt_data = []
for s in SAMPLE:
    results = []
    for t in range(TRIALS):
        sample = random.sample(VOTES, s)
        one_count = sum([1 for v in sample if v == 1])
        results.append(int(one_count > s/2))
    print(s, sum(results)/TRIALS)
    plt_data.append(sum(results)/TRIALS)

    
f, ax = plt.subplots(figsize=(7,4))
ax.plot(SAMPLE, plt_data)
ax.set_xlabel('sample size')
ax.set_ylabel('probability of +1 majority')
ax.grid()
plt.savefig(args.output, bbox_inches='tight')

#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

from collections import defaultdict

import pprint
pp = pprint.PrettyPrinter(indent=4)

# set up a tree
adapters = []
with open(filename, 'r') as file:
    adapters = sorted([int(line.rstrip()) for line in file])
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
pp.pprint(adapters)

def count_differences(adapters):
    diffs = defaultdict(int)
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        diffs[diff] += 1
    return diffs

diffs = count_differences(adapters)
print(diffs)
print(f'answer = {diffs[3] * diffs[1]}')

def count_arrangements(adapters):
    streaks = []
    streak = set()
    for i in range(1, len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i - 1]
        if diff < 3: # my neighbors can surive without me
            streak.add(adapters[i])
        else:
            if len(streak):
                streaks.append(streak)
            streak = set()
    else:
        if len(streak):
            streaks.append(streak)

    arrs = 1
    for streak in streaks:
        if len(streak) == 1:
            arrs *= 2 # two options, with and without
        elif len(streak) == 2:
            arrs *= 4 # both, either x 2, neither
        elif len(streak) == 3:
            arrs *= 7 # would be 8 but "none of the above" would leave a gap too big
    return arrs

arrs = count_arrangements(adapters)
print(f'arrangements = {arrs}')

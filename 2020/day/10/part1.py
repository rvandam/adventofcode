#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

from collections import defaultdict

import pprint
pp = pprint.PrettyPrinter(indent=4)

# set up a tree
adapters = []
with open(filename, 'r') as file:
    adapters = [int(line.rstrip()) for line in file]
pp.pprint(adapters)

def count_differences(adapters):
    sorted_adapters = sorted(adapters)
    diffs = {1: 1, 3: 1} # assume first (1) and last (3)
    for i in range(1, len(sorted_adapters)):
        diff = sorted_adapters[i] - sorted_adapters[i - 1]
        diffs[diff] += 1
    return diffs

diffs = count_differences(adapters)
print(diffs)
print(f'answer = {diffs[3] * diffs[1]}')

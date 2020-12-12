#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
preamble = int(sys.argv[2]) if len(sys.argv) > 2 else 25

from collections import defaultdict

import pprint
pp = pprint.PrettyPrinter(indent=4)

# set up a tree
nums = []
with open(filename, 'r') as file:
    nums = [int(line.rstrip()) for line in file]
pp.pprint(nums)


line = preamble
while line < len(nums):
    found = False
    for i in range(preamble):
        for j in range(preamble):
            if i == j: continue
            a = nums[line - i - 1]
            b = nums[line - j - 1]
#            print(f'does {a} + {b} == {nums[line]}')
            if a + b == nums[line]:
                found = True
    if not found:
        print(f'failed to find pair for {nums[line]}')
    line += 1

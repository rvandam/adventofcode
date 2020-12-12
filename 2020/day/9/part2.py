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
#pp.pprint(nums)


def find_weakness():
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
            return nums[line]
        line += 1

weakness = find_weakness()

start = 0
end = 1
sum = nums[start] + nums[end]
while end < len(nums):
    if sum < weakness:
        end += 1
        sum += nums[end]
    elif sum > weakness:
        sum -= nums[start]
        start += 1
    else:
        break

cont = sorted([nums[i] for i in range(start, end + 1)])
print(cont)
smallest = cont[0]
largest = cont[-1]
print(f'smallest = {smallest}, largest = {largest}, weaknes = {smallest + largest}')

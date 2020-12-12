#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

from collections import defaultdict

import pprint
pp = pprint.PrettyPrinter(indent=4)

# set up a tree
layout = []
with open(filename, 'r') as file:
    layout = [[c for c in line.rstrip()] for line in file]
#pp.pprint(layout)


def seat(cur, count):
    if cur == 'L' and count == 0:
        return '#'
    elif cur == '#' and count >= 4:
        return 'L'

def apply_rules(layout):
    changes = False
    counts = seat_counts(layout)
#    pp.pprint(counts)
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            new_seat = seat(layout[i][j], counts[i][j])
            if new_seat:
                changes = True
                layout[i][j] = new_seat
#    print(changes)
    return changes


# generate a map of seat counts in one pass
def seat_counts(layout):
    num_rows = len(layout)
    num_cols = len(layout[0])
    counts = [[0]*num_cols for x in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            if layout[i][j] != '#':
                continue # no seat to count
            # add one to each neighbor
            for i1 in range(i - 1, i + 2):
                for j1 in range (j - 1, j + 2):
                    # ignore self
                    if i == i1 and j == j1:
                        continue
                    # out of bounds
                    if i1 < 0 or i1 >= num_rows or j1 < 0 or j1 >= num_cols:
                        continue
#                    print(f'i = {i}, j = {j}, i1 = {i1}, j1 = {j1}')
                    counts[i1][j1] += 1
    return counts

def count_seats(layout):
    count = 0
    for x in layout:
        for y in x:
            if y == '#':
                count += 1 
    return count

changes = True
while changes:
    changes = apply_rules(layout)

#pp.pprint(layout)
print(f'seat count = {count_seats(layout)}')

#def count_differences(adapters):
#    sorted_adapters = sorted(adapters)
#    diffs = {1: 1, 3: 1} # assume first (1) and last (3)
#    for i in range(1, len(sorted_adapters)):
#        diff = sorted_adapters[i] - sorted_adapters[i - 1]
#        diffs[diff] += 1
#    return diffs
#
#diffs = count_differences(adapters)
#print(diffs)
#print(f'answer = {diffs[3] * diffs[1]}')

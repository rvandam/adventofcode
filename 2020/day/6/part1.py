#!/usr/bin/env python3

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

total = 0
with open(filename, 'r') as file:
    group = {}
    for line in file:
        line = line.rstrip()
        if line == '':
#            print(group)
            total += len(group)
            group = {}
        else:
            group.update({x:1 for x in line})
    else:
        total += len(group)
print(f'total = {total}')

#!/usr/bin/env python3

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
default_group = set({x for x in 'abcdefghijklmnopqrstuvwxyz'})

total = 0
with open(filename, 'r') as file:
    group = set(default_group)
    for line in file:
        line = line.rstrip()
        new_set = {x for x in line}
#        print(new_set)
        if line == '':
#            print(f'group final = {group}')
            total += len(group)
            group = set(default_group)
        else:
            group &= new_set
#            print(f'group now = {group}')
    else:
        total += len(group)
print(f'total = {total}')

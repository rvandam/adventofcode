#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

import re
pattern = re.compile('([NSEWLRF])(\d+)')

import pprint
pp = pprint.PrettyPrinter(indent=4)


def parse(line):
    m = pattern.match(line)
    return [m.group(1), int(m.group(2))]


earliest = 0
buses = []
with open(filename, 'r') as file:
    earliest = int(file.readline())
    buses = sorted([int(x) for x in file.readline().split(',') if x != 'x'])
pp.pprint(buses)

soonest = [0, earliest+buses[-1]]
for bus in buses:
    prev = (earliest // bus) * bus
    next = prev + bus
    if next < soonest[1]:
        soonest = [bus, next]

wait = soonest[1] - earliest
print(f'answer = {wait * soonest[0]}')
#
#dirs = {
#    'N': [-1, 0],
#    'S': [1, 0],
#    'E': [0, 1],
#    'W': [0, -1],
#}
#
#turns = {
#    'N': { 'L': 'W', 'R': 'E' },
#    'S': { 'L': 'E', 'R': 'W' },
#    'E': { 'L': 'N', 'R': 'S' },
#    'W': { 'L': 'S', 'R': 'N' },
#}
#
#pos = [0, 0]
#facing = 'E'
#
#for action in actions:
#    new_pos = pos
#    if action[0] in ['N', 'S', 'E', 'W']:
#        move = dirs[action[0]]
#        new_pos = [pos[i] + (move[i] * action[1]) for i in range(2)]
#    elif action[0] == 'F':
#        new_pos = [pos[i] + (dirs[facing][i] * action[1]) for i in range(2)]
#    elif action[0] in ['L', 'R']:
#        for i in range(0, action[1], 90):
#            facing = turns[facing][action[0]]
#                
#
#    print(f'pos {pos} + action {action} = pos {new_pos} (facing {facing})')
#    pos = new_pos
#
#print(f'manhattan = {abs(pos[0]) + abs(pos[1])}')

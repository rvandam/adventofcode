#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

import re
pattern = re.compile('([NSEWLRF])(\d+)')

import pprint
pp = pprint.PrettyPrinter(indent=4)

import math


def parse(line):
    m = pattern.match(line)
    return [m.group(1), int(m.group(2))]

actions = []
with open(filename, 'r') as file:
    actions = [parse(line) for line in file]
#pp.pprint(actions)

dirs = {
    'N': [-1, 0],
    'S': [1, 0],
    'E': [0, 1],
    'W': [0, -1],
}

pos = [0, 0]
waypoint = [-1, 10]

def rotateL(waypoint, pos):
    return [
        -waypoint[1],
        waypoint[0],
    ]

def rotateR(waypoint, pos):
    return [
        waypoint[1],
        -waypoint[0],
    ]

for action in actions:
    if action[0] in ['N', 'S', 'E', 'W']:
        move = dirs[action[0]]
        waypoint = [waypoint[i] + (move[i] * action[1]) for i in range(2)]
    elif action[0] == 'F':
        for i in range(action[1]):
            pos = [pos[i] + waypoint[i] for i in range(2)]
    elif action[0] == 'L':
        for i in range(0, action[1], 90):
            waypoint = rotateL(waypoint, pos)
    elif action[0] == 'R':
        for i in range(0, action[1], 90):
            waypoint = rotateR(waypoint, pos)
                

    print(f'action {action}, pos = {pos}, waypoint = {waypoint}')

print(f'manhattan = {abs(pos[0]) + abs(pos[1])}')

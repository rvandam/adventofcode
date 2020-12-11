#!/usr/bin/env python3

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

import re
pattern = re.compile('(?P<parent>\w+ \w+) bags contain (?P<children>((\d+ \w+ \w+|no other) bags?(, )?)*)\.')
child_pattern = re.compile('((?P<count>\d+) (?P<name>\w+ \w+)|no other) bags?')

from collections import defaultdict
#import networkx as nx
#graph = nx.DiGraph()

import pprint
pp = pprint.PrettyPrinter(indent=4)

# set up a tree
ops = []
with open(filename, 'r') as file:
    for line in file:
        line = line.rstrip()
        ops.append(tuple(line.split()))
pp.pprint(ops)


acc = 0
seen = defaultdict(int)
line = 0
while (not seen[line]):
    seen[line] += 1
    (op, arg) = ops[line]
    pp.pprint({ 'op':op, 'arg':arg, 'acc':acc, 'line':line })
    if op == 'acc':
        acc += int(arg)
        line += 1
    elif op == 'jmp':
        line += int(arg)
    else:
        line += 1
print(f'acc = {acc}')
#
#
#        m = pattern.match(line).groupdict()
#        if m:
#            for child in m['children'].split(', '):
#                cm = child_pattern.match(child).groupdict()
#                tree[cm['name']].add(m['parent'])
##pp.pprint(tree)
#
## now find the paths to 'shiny gold'
#start = set(tree['shiny gold'])
#changed = True
#while len(start):
#    start_len = len(start)
#    for item in set(start):
#        start |= tree[item]
#    if len(start) == start_len:
#        break;
#
#
#pp.pprint(start)
#print(f'size = {len(start)}')

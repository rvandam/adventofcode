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
#pp.pprint(ops)


def halting(ops):
    acc = 0
    seen = defaultdict(int)
    line = 0
    while (line < len(ops) and not seen[line]):
        seen[line] += 1
        (op, arg) = ops[line]
    #    pp.pprint({ 'op':op, 'arg':arg, 'acc':acc, 'line':line })
        if op == 'acc':
            acc += int(arg)
            line += 1
        elif op == 'jmp':
            line += int(arg)
        else:
            line += 1
    print(f'line = {line}')
    print(f'acc = {acc}')
    return line == len(ops)

def flip(pair):
    return ('jmp' if pair[0] == 'nop' else 'nop', pair[1])

for i in range(len(ops)):
    if ops[i][0] == 'acc': continue # nothing to do
    clone = list(ops)
    clone[i] = flip(clone[i])
    halts = halting(clone)
    print(f'line {i} modified program halts = {halts}')
    if halts: break

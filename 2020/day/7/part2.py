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

bags = defaultdict(list)

def bag_size(bag):
    size = 1
    for child in bags[bag]:
        size += child[1] * bag_size(child[0])
    return size

def bag_contains(bag):
    return bag_size(bag) - 1

with open(filename, 'r') as file:
    for line in file:
        m = pattern.match(line).groupdict()
        if m:
            for child in m['children'].split(', '):
                cm = child_pattern.match(child).groupdict()
                print(cm)
                if cm:
                    bags[m['parent']].append((cm['name'], int(cm['count'] or 0)))
pp.pprint(bags)

print(f"shiny gold contains {bag_contains('shiny gold')} bags")

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

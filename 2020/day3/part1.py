#!/usr/bin/env python3

tree = '#'
over = 3

trees = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        trees.append(line)

cols = len(trees[0])

found = 0
for i in range(len(trees)):
#    print(f'i = {i}, row = {i}, col = {i * over}')
#    print(f'char = {trees[i][(i * over) % cols]}')
    found += trees[i][(i * over) % cols] == tree

print(f'found = {found}')

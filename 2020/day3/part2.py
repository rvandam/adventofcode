#!/usr/bin/env python3

tree = '#'

trees = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        trees.append(line)

cols = len(trees[0])

multiple = 1
for down, right in [[1, 1], [1,3], [1, 5], [1, 7], [2, 1]]:
    found = 0
    for i in range(int(len(trees) / down)):
#       print(f'i = {i}, row = {i}, col = {i * right}')
#        print(f'char = {trees[i][(i * right) % cols]}')
        found += trees[i * down][(i * right) % cols] == tree
    print(f'Righ {right}, down {down} = {found}')
    multiple *= found

print(f'multipe = {multiple}')

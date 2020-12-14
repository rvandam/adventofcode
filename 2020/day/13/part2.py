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
bus_sets = []
with open(filename, 'r') as file:
    earliest = int(file.readline())
    for line in file:
        bus_sets.append([0 if x == 'x' else int(x) for x in line.split(',')])
#pp.pprint(bus_sets)

# chinese remainder theorem
# x mod n1 = a1
# x mod n2 = a2
# x mod n3 = a3
# ...
# x mod n1n2n3 = a1,3

# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
from functools import reduce
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1


for buses in bus_sets:
    ns = 1
    n = []
    a = []
    for i in range(len(buses)):
        if buses[i]:
            ns *= buses[i]
            n.append(buses[i])
            remainder = -i % buses[i]
            a.append(remainder)
            print(f'x mod {buses[i]} = {remainder}')
    crt = chinese_remainder(n, a)
    print(f"{crt} = {a} mod {n} ({ns})")
    print(f'x = {ns}n + {crt}')
    print(f'x mod {ns} = {crt}')
    print()

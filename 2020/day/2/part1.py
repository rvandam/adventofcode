#!/usr/bin/env python3

import re
pattern = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)');

valid = 0
invalid = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        m = pattern.search(line).groupdict()
        if int(m['min']) <= m['pass'].count(m['char']) <= int(m['max']):
            valid += 1
#            print(f'{line} is valid')
        else:
            invalid += 1
#            print(f'{line} is invalid')
#        print(f"\tmin = {m['min']}")
#        print(f"\tcount = {m['pass'].count(m['char'])}")
#        print(f"\tmax = {m['max']}")

print(f'valid = {valid}')
print(f'invalid = {invalid}')

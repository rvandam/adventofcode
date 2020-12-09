#!/usr/bin/env python3

import re
pattern = re.compile('(?P<pos1>\d+)-(?P<pos2>\d+) (?P<char>\w): (?P<pass>\w+)');

valid = 0
invalid = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        m = pattern.search(line).groupdict()
        p1 = int(m['pos1'])
        p2 = int(m['pos2'])
        ok1 = p1 <= len(m['pass']) and m['pass'][p1 - 1] == m['char']
        ok2 = p2 <= len(m['pass']) and m['pass'][p2 - 1] == m['char']
        if ok1 != ok2:
            valid += 1
#            print(f'{line} is valid')
        else:
            invalid += 1
#            print(f'{line} is invalid')
#        print(f"\tp1 = {p1}, ok1 = {ok1}")
#        print(f"\tp2 = {p2}, ok2 = {ok2}")

print(f'valid = {valid}')
print(f'invalid = {invalid}')

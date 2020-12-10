#!/usr/bin/env python3

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

required = tuple('byr iyr eyr hgt hcl ecl pid'.split())
optional = tuple('cid'.split())

passports = []
with open(filename, 'r') as file:
    passport = {}
    for line in file:
        line = line.rstrip()
        if (not line):
            passports.append(passport)
            passport = {}
            continue
        else:
            passport.update(dict(pair.split(':') for pair in line.split(' ')))
    else:
        passports.append(passport)

valid = 0
invalid = 0
for passport in passports:
    if all(x in passport for x in required):
        valid += 1
    else:
        invalid += 1

print(f'valid = {valid}')
print(f'invalid = {invalid}')

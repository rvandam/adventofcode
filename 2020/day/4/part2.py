#!/usr/bin/env python3

import sys
from cerberus import Validator

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

required = tuple('byr iyr eyr hgt hcl ecl pid'.split())
optional = tuple('cid'.split())

schema = {
    'byr': { 'required': True, 'type': 'integer', 'coerce': int, 'min': 1920, 'max': 2002 },
    'iyr': { 'required': True, 'type': 'integer', 'coerce': int, 'min': 2010, 'max': 2020 },
    'eyr': { 'required': True, 'type': 'integer', 'coerce': int, 'min': 2020, 'max': 2030 },
    'hgt': { 'required': True, 'type': 'string', 'regex': '^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$'}, # use coerce and customer validator instead?
    'hcl': { 'required': True, 'type': 'string', 'regex': '^#[a-f0-9]{6}$' },
    'ecl': { 'required': True, 'type': 'string', 'allowed': 'amb blu brn gry grn hzl oth'.split() },
    'pid': { 'required': True, 'type': 'string', 'regex': '^\d{9}$' },
    'cid': { 'required': False },
}
v = Validator(schema)


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
    if v.validate(passport):
        valid += 1
    else:
#        print(passport)
#        print(v.errors)
        invalid += 1

print(f'valid = {valid}')
print(f'invalid = {invalid}')

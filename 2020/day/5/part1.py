#!/usr/bin/env python3

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

def calc_seat_id(boarding):
    row = 0
    col = 0
    for i in range(7):
        digit = 1 if boarding[i] == 'B' else 0
        row += digit * (2 ** (6 - i))
    for i in range(3):
        digit = 1 if boarding[i+7] == 'R' else 0
        col += digit * (2 ** (2 - i))
    return (row, col, row * 8 + col)

highest = 0
with open(filename, 'r') as file:
    for line in file:
        line = line.rstrip()
        (row, col, seat_id) = calc_seat_id(line)
        print(f'{line}: row {row}, column {col}, seat ID {seat_id}')
        if seat_id > highest: highest = seat_id
print(f'highest = {highest}')

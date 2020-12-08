expenses = []

with open('input.txt', 'r') as file:
    # read lines, parse ints and sort (so we can short circuit lookups later)
    expenses = sorted([int(line) for line in file])

    # can't think of a clever solution for 3 numbers so brute force it is :(
    for e1 in expenses:
        for e2 in expenses:
            if e2 <= e1: continue
            for e3 in expenses:
                if e3 <= e2: continue
                if e1 + e2 + e3 == 2020: print(f'{e1} * {e2} * {e3} = {e1 * e2 * e3}')

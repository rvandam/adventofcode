expenses = []

with open('input.txt', 'r') as file:
    # read lines, parse ints and sort (so we can short circuit lookups later)
    expenses = sorted([int(line) for line in file])
    # make a lookup table of pairs that sum to 2020
    lookup = {(2020 - i):i for i in expenses}
    # check if any pairs exist
    for e in expenses:
        e2 = lookup.get(e) # does my pair exist
        if (not e2):
            continue # if not, next number
        elif (e2 < e):
            break # every pair will exist twice, once we cross the midpoint, we're done
        else:
            print(f'{e} * {e2} = {e * e2}') # print result if found

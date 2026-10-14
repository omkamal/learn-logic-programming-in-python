# the same function on a bill with one slip: a wheel "contains" a bicycle
HAS = {
    'bicycle': {'frame': 1, 'wheel': 2},
    'wheel': {'spoke': 32, 'bicycle': 1},
}

def total_in(assembly):
    found = {}
    for sub, how_many in HAS.get(assembly, {}).items():
        found[sub] = found.get(sub, 0) + how_many
        for part, count in total_in(sub).items():
            found[part] = found.get(part, 0) + how_many * count
    return found

try:
    print(total_in('bicycle'))
except RecursionError as error:
    print('RecursionError:', error)

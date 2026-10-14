line = {'CAI': ['DXB'], 'DXB': ['LHR'], 'LHR': ['JFK']}
loop = {'CAI': ['DXB'], 'DXB': ['LHR'], 'LHR': ['JFK', 'CAI']}

def where_can(flights, city):          # one desk answers for one city
    found = set()
    for nxt in flights.get(city, []):  # take one flight ...
        found |= {nxt} | where_can(flights, nxt)   # ... ask the next desk
    return found

print(sorted(where_can(line, 'CAI')))
try:
    print(sorted(where_can(loop, 'CAI')))
except RecursionError as err:
    print('RecursionError:', err)

def where_can_seen(flights, city):     # the same, with a notebook
    seen, todo = set(), [city]
    while todo:
        for nxt in flights.get(todo.pop(), []):
            if nxt not in seen:        # new city: write it down
                seen.add(nxt)
                todo.append(nxt)
    return seen

print(sorted(where_can_seen(loop, 'CAI')))

import sys
print('recursion limit:', sys.getrecursionlimit())

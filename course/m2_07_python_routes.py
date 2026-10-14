flights = {'CAI': ['DXB'], 'DXB': ['LHR'], 'LHR': ['CAI', 'JFK']}

# naive recursion: follow every flight, remember nothing
def reach_naive(city):
    found = set()
    for nxt in flights.get(city, []):
        found |= {nxt} | reach_naive(nxt)
    return found

try:
    print(sorted(reach_naive('CAI')))
except RecursionError as err:
    print('RecursionError:', err)

# the fix: a to-do list plus a set of cities already seen
def reach(city):
    seen, todo = set(), [city]
    while todo:
        for nxt in flights.get(todo.pop(), []):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen

print(sorted(reach('CAI')))

import sys

flights = {'CAI': ['DXB'], 'DXB': ['LHR'], 'LHR': ['JFK', 'CAI']}


def where_can(city):               # remembers nothing
    found = set()
    for nxt in flights.get(city, []):
        found.add(nxt)
        found |= where_can(nxt)
    return found


print(sys.getrecursionlimit())
try:
    print(sorted(where_can('CAI')))
except RecursionError as err:
    print(type(err).__name__ + ':', err)

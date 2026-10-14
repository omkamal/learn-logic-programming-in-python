from pyDatalog import pyDatalog

flights = [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'), ('LHR', 'CAI')]

# the notebook of cities reached from CAI, round by round
notebook = {b for a, b in flights if a == 'CAI'}     # round 1
print('round 1: new', sorted(notebook))
n = 1
while True:
    n += 1
    new = {y for (z, y) in flights if z in notebook} - notebook
    print(f'round {n}: new', sorted(new))
    if not new:                         # nothing new: stop
        break
    notebook |= new

# the same question, asked of pyDatalog (recursive literal FIRST)
pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in flights:
    +flight(a, b)
reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)
print('engine agrees:', notebook == {y for (y,) in reach('CAI', Y).data})

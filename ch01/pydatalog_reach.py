from pyDatalog import pyDatalog

pyDatalog.create_terms('flight, reach, X, Y, Z')

+flight('CAI', 'DXB')
+flight('DXB', 'LHR')
+flight('LHR', 'CAI')
+flight('LHR', 'JFK')

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)    # the recursive condition first

print(sorted(reach('CAI', Y).data))          # which cities does CAI reach?
print(bool(reach('CAI', 'JFK')))             # a yes/no question

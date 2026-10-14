from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, bound_first, negation_first')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

# city(Y) gives Y a value BEFORE the negation looks at it
bound_first(Y) <= city(Y) & ~reach('CAI', Y) & (Y != 'CAI')
print(sorted(bound_first(Y).data))

# the negation comes first, while Y has no value yet
negation_first(Y) <= ~reach('CAI', Y) & city(Y) & (Y != 'CAI')
print(sorted(negation_first(Y).data))

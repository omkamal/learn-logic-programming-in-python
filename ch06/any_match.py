from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, no_flight_out')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

# Y appears only inside the ~ : "is there ANY flight out of X?"
no_flight_out(X) <= city(X) & ~flight(X, Y)

print(sorted(no_flight_out(X).data))

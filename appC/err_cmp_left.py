from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, P, fare, cheap')
+fare('CAI', 'DXB', 150)
+fare('LHR', 'CAI', 180)

cheap(A, B) <= (P < 200) & fare(A, B, P)     # check before fill
try:
    print(cheap(A, B))
except Exception as err:
    print(type(err).__name__ + ':', err)

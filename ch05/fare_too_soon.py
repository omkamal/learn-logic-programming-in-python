from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, P, T, fare, cheap, total')
+fare('CAI', 'DXB', 150)
+fare('DXB', 'LHR', 320)
+fare('LHR', 'JFK', 410)
+fare('LHR', 'CAI', 180)

cheap(A, B) <= (P < 200) & fare(A, B, P)      # check before fill
try:
    print(sorted(cheap(A, B).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])

total(A, B, T) <= (T == P + 25) & fare(A, B, P)   # calculate before fill
print(sorted(total(A, B, T).data))

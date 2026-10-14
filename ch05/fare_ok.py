from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, P, T, fare, cheap, total')
+fare('CAI', 'DXB', 150)
+fare('DXB', 'LHR', 320)
+fare('LHR', 'JFK', 410)
+fare('LHR', 'CAI', 180)

# the table literal first; the check or the calculation after it
cheap(A, B) <= fare(A, B, P) & (P < 200)
total(A, B, T) <= fare(A, B, P) & (T == P + 25)

print(sorted(cheap(A, B).data))
for row in sorted(total(A, B, T).data):
    print(row)

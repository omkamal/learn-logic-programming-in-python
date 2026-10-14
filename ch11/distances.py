import math
from pyDatalog import pyDatalog

def km(lat1, lon1, lat2, lon2):
    """Great-circle distance in kilometers (haversine formula)."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    h = math.sin(dp / 2) ** 2
    h += math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))

def show(rows):                 # whole kilometers, for people
    for a, b, d in sorted(rows):
        print(a, b, round(d), 'km')

pyDatalog.create_terms('A, B, D, La, Lo, Lb, Mo, where, flight, far')
pyDatalog.create_terms('dist, km')

# approximate city-center coordinates, degrees north and east
+where('CAI', 30.04, 31.24)
+where('DXB', 25.20, 55.27)
+where('LHR', 51.51, -0.13)
+where('JFK', 40.71, -74.01)
+where('NRT', 35.68, 139.65)
+flight('CAI', 'DXB')
+flight('DXB', 'LHR')
+flight('LHR', 'JFK')

dist(A, B, D) <= (flight(A, B) & where(A, La, Lo) & where(B, Lb, Mo) &
                  (D == km(La, Lo, Lb, Mo)))
far(A, B) <= dist(A, B, D) & (D > 5000)

show(dist(A, B, D).data)
print('over 5000 km:', sorted(far(A, B).data))

+flight('JFK', 'NRT')                  # one new fact, no new rule
show([r for r in dist(A, B, D).data if r[0] == 'JFK'])

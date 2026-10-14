from pyDatalog import pyDatalog

pyDatalog.create_terms('N, L, lucas')
+(lucas[0] == 2)
+(lucas[1] == 1)
lucas[N] = lucas[N - 1] + lucas[N - 2]

def at(query):
    return query.data[0][0]

print([(n, at(lucas[n] == L)) for n in range(2, 6)])

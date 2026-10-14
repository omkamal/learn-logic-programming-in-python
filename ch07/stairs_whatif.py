from pyDatalog import pyDatalog

pyDatalog.create_terms('N, W, ways3')

+(ways3[0] == 1)                 # hops of 1, 2 or 3 stairs
+(ways3[1] == 1)
+(ways3[2] == 2)                 # one more ground floor
ways3[N] = ways3[N - 1] + ways3[N - 2] + ways3[N - 3]

def at(query):
    return query.data[0][0]

print([(n, at(ways3[n] == W)) for n in range(1, 9)])

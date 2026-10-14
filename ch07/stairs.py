from pyDatalog import pyDatalog

pyDatalog.create_terms('N, W, ways')

+(ways[0] == 1)                  # one way to climb nothing: stand still
+(ways[1] == 1)                  # one way to climb one stair
ways[N] = ways[N - 1] + ways[N - 2]   # last hop was 1 stair or 2 stairs

def at(query):
    return query.data[0][0]

print([(n, at(ways[n] == W)) for n in range(1, 9)])
print(at(ways[30] == W))

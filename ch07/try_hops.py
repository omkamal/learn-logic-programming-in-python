from pyDatalog import pyDatalog

pyDatalog.create_terms('N, W, ways')
+(ways[0] == 1)                  # stand still
+(ways[1] == 0)                  # a single stair cannot be climbed
+(ways[2] == 1)
ways[N] = ways[N - 2] + ways[N - 3]

def at(query):
    return query.data[0][0]

print([(n, at(ways[n] == W)) for n in range(1, 8)])

def hops(n):                     # brute force, hops of 2 or 3 only
    if n == 0:
        return [()]
    return [(h,) + rest for h in (2, 3) if h <= n for rest in hops(n - h)]

print([(n, len(hops(n))) for n in range(1, 8)])

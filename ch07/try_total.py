from pyDatalog import pyDatalog

pyDatalog.create_terms('N, S, total_to')
+(total_to[0] == 0)
total_to[N] = N + total_to[N - 1]

def at(query):
    return query.data[0][0]

print(at(total_to[4] == S), at(total_to[100] == S), 100 * 101 // 2)

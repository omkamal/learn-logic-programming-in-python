from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, Y, factorial, sq, cost')

+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]
sq[N] = N * N
+(cost['book'] == 12)

print(sorted((cost[N] == 12).data))        # a stored value: both ways
print(sq[7] == Y)                          # a computed value: forward
print(sorted((sq[N] == 49).data))          # ...but not backward
print(sorted((factorial[N] == 120).data))
print(sorted((factorial[N] == F).data))

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, cost, dcost')

+(cost['pen'] == 3)
+(cost['book'] == 12)

print(cost['pen'] == N)
print(sorted((cost[X] == N).data))

dcost[X] = cost[X] * 2
print(sorted((dcost[X] == N).data))

+(cost['pen'] == 4)              # a second price for the same pen
print(sorted((cost[X] == N).data))
print(sorted((dcost[X] == N).data))

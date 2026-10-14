from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, fib')

+(fib[0] == 0)                        # two ground floors
+(fib[1] == 1)
fib[N] = fib[N - 1] + fib[N - 2]      # the sum of the two below

print(fib[20] == F)
print(fib[100] == F)

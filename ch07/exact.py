import math
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial, fib')

+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]
+(fib[0] == 0)
+(fib[1] == 1)
fib[N] = fib[N - 1] + fib[N - 2]

def at(query):
    return query.data[0][0]

same = all(at(factorial[n] == F) == math.factorial(n) for n in range(26))
print('factorial 0..25 equal Python:', same)
print(at(factorial[25] == F))

a, b = 0, 1
for _ in range(300):
    a, b = b, a + b
print('fib[300] equals Python:', at(fib[300] == F) == a)

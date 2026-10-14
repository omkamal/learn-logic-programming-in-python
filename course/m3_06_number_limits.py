from pyDatalog import pyDatalog

pyDatalog.create_terms('X, F, N, price, factorial')

# floats that pass through the engine
+price('a', 0.1)
+price('b', 12 * 0.14)
print(sorted(price(X, F).data))
print(0.1, 12 * 0.14)               # what plain Python holds

# integers that pass through the engine
+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]
for n in (20, 21, 25):
    print(n, (factorial[n] == F).data, "python:", __import__('math').factorial(n))

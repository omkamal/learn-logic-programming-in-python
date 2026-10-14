from pyDatalog import pyDatalog

def unit_price(total, count):
    return total // count

cheap = lambda cents: cents // 2

pyDatalog.create_terms('X, T, K, U, pack, each, half, ratio')
pyDatalog.create_terms('unit_price, cheap')

+pack('box', 1200, 4)
+pack('empty', 500, 0)

# a bug inside the function: the empty pack divides by zero
each(X, U) <= pack(X, T, K) & (U == unit_price(T, K))
rows = sorted(each(X, U).data)
print(*rows, sep='\n')

# the same question asked through a lambda that was named
half(X, U) <= pack(X, T, K) & (U == cheap(T))
print(*sorted(half(X, U).data, key=str), sep='\n')

# no function of ours at all: plain rule arithmetic does it too
ratio(X, U) <= pack(X, T, K) & (U == T / K)
print(*sorted(ratio(X, U).data), sep='\n')

failed = [r for r in rows if any(isinstance(v, Exception) for v in r)]
print(failed)

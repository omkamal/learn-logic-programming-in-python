from pyDatalog import pyDatalog

seen = []

def twice(v):
    seen.append(v)
    return v * 2

pyDatalog.create_terms('I, N, T, num, big, twice')

for i, v in enumerate([1, 5, 10, 20]):
    +num(i, v)

# the comparison (N > 5) is written BEFORE the call
big(I, T) <= num(I, N) & (N > 5) & (T == twice(N))
print(sorted(big(I, T).data))
print('the function saw', sorted(seen))

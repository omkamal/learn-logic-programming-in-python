# Brute force: list every sequence of hops of 1 or 2 stairs.
def hops(n, allowed=(1, 2)):
    if n == 0:
        return [()]
    return [(h,) + rest for h in allowed if h <= n
            for rest in hops(n - h, allowed)]

for seq in hops(4):
    print(seq)

print([(n, len(hops(n))) for n in range(1, 9)])

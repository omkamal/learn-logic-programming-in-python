# timeout: 120
import random
from pyDatalog import pyDatalog

def python_totals(edges):
    """Reference answer: plain Python recursion with a dictionary."""
    kids = {}
    for a, p, n in edges:
        kids.setdefault(a, []).append((p, n))
    def inside(a):                    # {part: how many in one a}
        found = {}
        for q, m in kids.get(a, []):
            found[q] = found.get(q, 0) + m
            for p, c in inside(q).items():
                found[p] = found.get(p, 0) + m * c
        return found
    names = {x for e in edges for x in e[:2]}
    return {(a, p): c for a in names for p, c in inside(a).items()}

def random_bill(seed, size=7):
    rnd = random.Random(seed)
    names = [f'n{i}' for i in range(size)]
    return [(names[i], names[j], rnd.choice([1, 2, 2, 3, 4]))
            for i in range(size) for j in range(i + 1, size)
            if rnd.random() < 0.4]

tested = ok_route = ok_levels = ok_naive = 0
for seed in range(60):
    edges = random_bill(seed)
    if not edges:
        continue
    want = python_totals(edges)
    pyDatalog.clear()       # (module level: create_terms needs it)
    pyDatalog.create_terms('A, P, Q, N, M, K, R, S, T, C, has, route')
    pyDatalog.create_terms('uses, total, naive, part, count')
    for a, p, n in edges:
        +has(a, p, n)
    route(A, P, S, N) <= has(A, P, N) & (S == A + '>' + P)
    route(A, P, S, N) <= (route(A, Q, R, M) & has(Q, P, K)
                          & (N == M * K) & (S == R + '>' + P))
    (total[A, P] == sum_(N, for_each=S)) <= route(A, P, S, N)
    part(P) <= has(P, Q, N)
    part(P) <= has(Q, P, N)
    (count[P, P] == 1) <= part(P)
    (count[A, P] == sum_(T, for_each=Q)) <= (has(A, Q, M)
                                             & (C == count[Q, P])
                                             & (T == M * C))
    uses(A, P, N) <= has(A, P, N)
    uses(A, P, N) <= uses(A, Q, M) & has(Q, P, K) & (N == M * K)
    (naive[A, P] == sum_(N, for_each=N)) <= uses(A, P, N)
    routes = {(a, p): n for a, p, n in (total[A, P] == N).data}
    levels = {(a, p): n for a, p, n in (count[A, P] == N).data if a != p}
    naive_ = {(a, p): n for a, p, n in (naive[A, P] == N).data}
    tested += 1
    ok_route += routes == want
    ok_levels += levels == want
    ok_naive += naive_ == want

print('random bills tested:', tested)
print('route + sum_ agrees with Python:    ', ok_route)
print('levels (recursive sum_) agrees:     ', ok_levels)
print('chain totals added by value agrees: ', ok_naive)

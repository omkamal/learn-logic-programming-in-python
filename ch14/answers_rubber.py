from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, R, S, has, route, total')
pyDatalog.create_terms('part, leaf, buy')

for assembly, piece, how_many in [
        ('bicycle', 'frame', 1), ('bicycle', 'wheel', 2),
        ('bicycle', 'handlebar', 1),
        ('wheel', 'rim', 1), ('wheel', 'tire', 1), ('wheel', 'hub', 1),
        ('wheel', 'spoke', 32),
        ('hub', 'axle', 1), ('hub', 'bearing', 2),
        ('frame', 'tube', 3), ('frame', 'bolt', 4),
        ('handlebar', 'grip', 2), ('handlebar', 'bolt', 4)]:
    +has(assembly, piece, how_many)
+has('grip', 'rubber', 1)           # the new fact: a grip is an assembly

route(A, P, S, N) <= has(A, P, N) & (S == A + '>' + P)
route(A, P, S, N) <= (route(A, Q, R, M) & has(Q, P, K)
                      & (N == M * K) & (S == R + '>' + P))
part(P) <= has(P, Q, N)
part(P) <= has(Q, P, N)
leaf(P) <= part(P) & ~has(P, Q, N)
(buy[P] == sum_(N, for_each=S)) <= route('bicycle', P, S, N) & leaf(P)

print('leaf parts:', sorted(row[0] for row in leaf(P).data))
for piece, n in sorted((buy[P] == N).data):
    print(f'{piece:8} {n}')

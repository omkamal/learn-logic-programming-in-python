from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, R, S')
pyDatalog.create_terms('has, route, total')

# has(assembly, part, how many go into ONE assembly)
for assembly, piece, how_many in [
        ('bicycle', 'frame', 1), ('bicycle', 'wheel', 2),
        ('bicycle', 'handlebar', 1),
        ('wheel', 'rim', 1), ('wheel', 'tire', 1), ('wheel', 'hub', 1),
        ('wheel', 'spoke', 32),
        ('hub', 'axle', 1), ('hub', 'bearing', 2),
        ('frame', 'tube', 3), ('frame', 'bolt', 4),
        ('handlebar', 'grip', 2), ('handlebar', 'bolt', 4)]:
    +has(assembly, piece, how_many)

# one fact per chain, and the chain is written into the fact
route(A, P, S, N) <= has(A, P, N) & (S == A + '>' + P)
route(A, P, S, N) <= (route(A, Q, R, M) & has(Q, P, K)
                      & (N == M * K) & (S == R + '>' + P))

# add the chains up: one number per chain, so none can merge
(total[A, P] == sum_(N, for_each=S)) <= route(A, P, S, N)

print(sorted(route('bicycle', 'bolt', S, N).data))
print('spokes in a bicycle:', (total['bicycle', 'spoke'] == N).data)
print('bolts in a bicycle: ', (total['bicycle', 'bolt'] == N).data)
print('spokes in a wheel:  ', (total['wheel', 'spoke'] == N).data)

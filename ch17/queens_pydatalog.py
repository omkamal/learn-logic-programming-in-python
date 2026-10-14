# Eight queens in pyDatalog: a copy of the course snippet m4_03_queens.py
# (re-wrapped to 76 columns, same logic).
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, X, Y, D, queen, ok, solution, col')
for c in range(8):
    +col(c)

# ok(X, Y, D): queens in columns X and Y that are D rows apart
# do not attack each other
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

pyDatalog.create_terms('A, B, C, E, F, G, H, I')
solution(A, B, C, E, F, G, H, I) <= (
    col(A) & col(B) & ok(A, B, 1) &
    col(C) & ok(A, C, 2) & ok(B, C, 1) &
    col(E) & ok(A, E, 3) & ok(B, E, 2) & ok(C, E, 1) &
    col(F) & ok(A, F, 4) & ok(B, F, 3) & ok(C, F, 2) & ok(E, F, 1) &
    col(G) & ok(A, G, 5) & ok(B, G, 4) & ok(C, G, 3) & ok(E, G, 2) &
    ok(F, G, 1) &
    col(H) & ok(A, H, 6) & ok(B, H, 5) & ok(C, H, 4) & ok(E, H, 3) &
    ok(F, H, 2) & ok(G, H, 1) &
    col(I) & ok(A, I, 7) & ok(B, I, 6) & ok(C, I, 5) & ok(E, I, 4) &
    ok(F, I, 3) & ok(G, I, 2) & ok(H, I, 1))

t = time.perf_counter()
answers = solution(A, B, C, E, F, G, H, I).data
print(len(answers), "solutions in", round(time.perf_counter() - t, 3), "s")
print(sorted(answers)[0])

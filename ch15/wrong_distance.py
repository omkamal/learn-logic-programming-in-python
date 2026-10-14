from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')
pyDatalog.create_terms('Q0, Q1, Q2, Q3')

for c in range(4):
    +col(c)

ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

solution(Q0, Q1, Q2, Q3) <= (
    col(Q0) &
    col(Q1) & ok(Q0, Q1, 1) &
    col(Q2) & ok(Q0, Q2, 1) & ok(Q1, Q2, 1) &
    col(Q3) & ok(Q0, Q3, 1) & ok(Q1, Q3, 1) & ok(Q2, Q3, 1))

print(len(solution(Q0, Q1, Q2, Q3).data), 'solutions')

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, Q0, Q1, Q2, Q3, col, ok, ok_cols, full,'
                       ' loose')
for c in range(4):
    +col(c)
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)
ok_cols(X, Y, D) <= (X != Y)                  # diagonals forgotten

full(Q0, Q1, Q2, Q3) <= (col(Q0) & col(Q1) & ok(Q0, Q1, 1)
                         & col(Q2) & ok(Q0, Q2, 2) & ok(Q1, Q2, 1)
                         & col(Q3) & ok(Q0, Q3, 3) & ok(Q1, Q3, 2)
                         & ok(Q2, Q3, 1))
loose(Q0, Q1, Q2, Q3) <= (col(Q0) & col(Q1) & ok_cols(Q0, Q1, 1)
                          & col(Q2) & ok_cols(Q0, Q2, 2)
                          & ok_cols(Q1, Q2, 1)
                          & col(Q3) & ok_cols(Q0, Q3, 3)
                          & ok_cols(Q1, Q3, 2) & ok_cols(Q2, Q3, 1))
print(len(full(Q0, Q1, Q2, Q3).data), 'boards with the full rule')
print(len(loose(Q0, Q1, Q2, Q3).data), 'boards with columns only')

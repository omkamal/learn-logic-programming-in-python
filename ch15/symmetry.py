from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')
pyDatalog.create_terms('Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7')

for c in range(8):
    +col(c)

ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

solution(Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7) <= (
    col(Q0) &
    col(Q1) & ok(Q0, Q1, 1) &
    col(Q2) & ok(Q0, Q2, 2) & ok(Q1, Q2, 1) &
    col(Q3) & ok(Q0, Q3, 3) & ok(Q1, Q3, 2) & ok(Q2, Q3, 1) &
    col(Q4) & ok(Q0, Q4, 4) & ok(Q1, Q4, 3) & ok(Q2, Q4, 2) &
              ok(Q3, Q4, 1) &
    col(Q5) & ok(Q0, Q5, 5) & ok(Q1, Q5, 4) & ok(Q2, Q5, 3) &
              ok(Q3, Q5, 2) & ok(Q4, Q5, 1) &
    col(Q6) & ok(Q0, Q6, 6) & ok(Q1, Q6, 5) & ok(Q2, Q6, 4) &
              ok(Q3, Q6, 3) & ok(Q4, Q6, 2) & ok(Q5, Q6, 1) &
    col(Q7) & ok(Q0, Q7, 7) & ok(Q1, Q7, 6) & ok(Q2, Q7, 5) &
              ok(Q3, Q7, 4) & ok(Q4, Q7, 3) & ok(Q5, Q7, 2) &
              ok(Q6, Q7, 1))

def squares(board):                    # (row, column) of every queen
    return {(row, c) for row, c in enumerate(board)}

def quarter_turn(queens):
    return {(c, 7 - row) for row, c in queens}

def mirror(queens):
    return {(row, 7 - c) for row, c in queens}

def look_alikes(board):                # the 8 ways to turn or flip it
    queens, images = squares(board), []
    for _ in range(4):
        queens = quarter_turn(queens)
        images += [sorted(queens), sorted(mirror(queens))]
    return images

solutions = solution(Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7).data
shapes = {tuple(min(look_alikes(board))) for board in solutions}
print(len(solutions), 'boards, but only', len(shapes), 'different shapes')

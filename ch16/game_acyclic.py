from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, move, win')

# a game graph a -> b -> c: you lose if you cannot move
+move('a', 'b')
+move('b', 'c')

# a position wins if some move leads to a position that does not win
win(X) <= move(X, Y) & ~win(Y)
print(sorted(win(X).data))

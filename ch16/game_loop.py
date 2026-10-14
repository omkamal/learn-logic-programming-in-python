# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, move, win')

# the same game, but now a and b can move back and forth forever
+move('a', 'b')
+move('b', 'a')

win(X) <= move(X, Y) & ~win(Y)
print(sorted(win(X).data))

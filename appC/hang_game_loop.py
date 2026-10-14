# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, move, win')
+move('a', 'b')
+move('b', 'a')                    # a and b can move back and forth

win(X) <= move(X, Y) & ~win(Y)     # win depends on its own negation
print('asking')
print(sorted(win(X).data))

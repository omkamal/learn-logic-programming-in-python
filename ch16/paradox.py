from pyDatalog import pyDatalog

pyDatalog.create_terms('X, q, p')

+q(1)
# p(1) holds if q(1) holds and p(1) does not hold: a contradiction
p(X) <= q(X) & ~p(X)
print(p(X).data)

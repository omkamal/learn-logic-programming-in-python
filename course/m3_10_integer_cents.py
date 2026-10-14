from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, pay, total, pay_cents, total_cents')

# monthly pay with cents, stored as floats
+pay('ann', 'eng', 1200.10)
+pay('bob', 'eng', 1000.20)
(total[Y] == sum_(N, for_each=X)) <= pay(X, Y, N)
print(sorted(total[Y] == Z), 'python:', 1200.10 + 1000.20)

# the same pay stored as integer cents
+pay_cents('ann', 'eng', 120010)
+pay_cents('bob', 'eng', 100020)
(total_cents[Y] == sum_(N, for_each=X)) <= pay_cents(X, Y, N)
print(sorted(total_cents[Y] == Z))

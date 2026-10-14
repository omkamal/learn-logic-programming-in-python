from pyDatalog import pyDatalog

pyDatalog.create_terms('X, F, price, cents')

+price('tenth', 0.1)
+cents('tenth', 10)
print(0.1, 'in Python;', price('tenth', F).data[0][0], 'from the engine')
print(cents('tenth', F).data[0][0], 'as integer cents: exact')

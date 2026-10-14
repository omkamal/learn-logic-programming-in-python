from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price')
+price('tenth', 0.1)
+price('ten', 10)

print(sorted((price(X, N)).data))

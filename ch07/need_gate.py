from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, price, pricey')

+price('pen', 3)
+price('book', 12)
+pricey('book')              # typed by hand: "this one costs a lot"

-price('pen', 3)             # the shop raises the price of the pen
+price('pen', 6)

print(sorted(price(X, N).data))
print(sorted(pricey(X).data))

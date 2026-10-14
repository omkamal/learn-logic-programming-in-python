import csv
import io

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, Q, T, price, line')
rows = csv.reader(io.StringIO('pen,300\nbook,1200\n'))
for item, cents in rows:
    +price(item, cents)            # cents is the text '300', not 300
+price('lamp', 1999)

line(X, T) <= price(X, N) & (T == 3 * N)
print(sorted(line(X, T).data))

from pyDatalog import pyDatalog

pyDatalog.create_terms('P, H, T, R, run, rnk')

+run('nina', 'h1', 61)
+run('omar', 'h1', 58)
+run('pia', 'h1', 65)
+run('quin', 'h2', 59)
+run('raj', 'h2', 57)

# the smallest time wins, so the sort is low to high: no minus sign
(rnk[P] == rank_(group_by=H, order_by=T)) <= run(P, H, T)
print(sorted((rnk[P] == R).data))

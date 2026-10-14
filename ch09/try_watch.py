from pyDatalog import pyDatalog

pyDatalog.create_terms('W, E, M, S, ep, cum, past, first_past')

+ep('orbit', 1, 22)
+ep('orbit', 2, 24)
+ep('orbit', 3, 25)
+ep('orbit', 4, 21)
+ep('tides', 1, 45)
+ep('tides', 2, 40)
+ep('tides', 3, 38)

(cum[W, E] == running_sum_(M, group_by=W, order_by=E)) <= ep(W, E, M)
past(W, E) <= (cum[W, E] == S) & (S >= 60)
(first_past[W] == min_(E, order_by=E)) <= past(W, E)

for row in sorted((cum[W, E] == S).data):
    print(row)
print(sorted((first_past[W] == E).data))

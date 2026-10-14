from pyDatalog import pyDatalog

pyDatalog.create_terms('T, R, G, S, pts, total')

+pts('owls', 1, 3)
+pts('owls', 2, 0)
+pts('owls', 3, 3)
+pts('owls', 4, 1)
+pts('lynx', 1, 1)
+pts('lynx', 2, 3)
+pts('lynx', 3, 3)
+pts('lynx', 4, 0)

(total[T, R] == running_sum_(G, group_by=T, order_by=R)) <= pts(T, R, G)
for row in sorted((total[T, R] == S).data):
    print(row)

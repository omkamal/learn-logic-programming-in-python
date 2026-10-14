from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, C, C1, C2, link, path, any_city, bad_path')

+link('CAI', 'DXB', 4)
+link('DXB', 'LHR', 7)
+link('CAI', 'LHR', 12)
+link('LHR', 'JFK', 8)
+link('DXB', 'JFK', 14)

path(X, Y, C) <= link(X, Y, C)
path(X, Y, C) <= path(X, Z, C1) & link(Z, Y, C2) & (C == C1 + C2)

# slip 1: the key names only the start, so every destination is pooled
(any_city[X] == min_(C, order_by=C)) <= path(X, Y, C)
print(sorted((any_city[X] == C).data))

# slip 2: the sum is written before C1 and C2 are filled in
bad_path(X, Y, C) <= link(X, Y, C)
bad_path(X, Y, C) <= (C == C1 + C2) & bad_path(X, Z, C1) & link(Z, Y, C2)
print(sorted(bad_path('CAI', 'JFK', C).data))
print(len(bad_path(X, Y, C).data), 'rows;', len(link(X, Y, C).data),
      'links')

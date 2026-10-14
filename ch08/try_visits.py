from pyDatalog import pyDatalog

pyDatalog.create_terms('V, P, S, Z, visit, spent, visits, longest')
for vid, page, secs in [(1, 'home', 30), (2, 'home', 45), (3, 'docs', 120),
                        (4, 'docs', 90), (5, 'docs', 60), (6, 'blog', 15)]:
    +visit(vid, page, secs)

(spent[P]   == sum_(S, for_each=V)) <= visit(V, P, S)
(visits[P]  == len_(V))             <= visit(V, P, S)
(longest[P] == max_(V, order_by=S)) <= visit(V, P, S)

print(sorted((spent[P] == Z).data))
print(sorted((visits[P] == Z).data))
print(sorted((longest[P] == Z).data))

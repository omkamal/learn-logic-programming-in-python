from pyDatalog import pyDatalog

pyDatalog.create_terms('X, C, H, Z, kid, tallest')
for name, cls, cm in [('ann', '7a', 152), ('bea', '7a', 148),
                      ('cal', '7a', 160), ('dev', '7b', 155),
                      ('eve', '7b', 158)]:
    +kid(name, cls, cm)

(tallest[C] == max_(X, order_by=H)) <= kid(X, C, H)
print(sorted((tallest[C] == Z).data))

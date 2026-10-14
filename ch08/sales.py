from pyDatalog import pyDatalog

pyDatalog.create_terms('I, R, N, Z, sale, revenue, orders, biggest,'
                       ' on_target')

for sid, region, amount in [(1, 'north', 50), (2, 'north', 70),
                            (3, 'south', 30), (4, 'south', 90),
                            (5, 'west', 60)]:
    +sale(sid, region, amount)

(revenue[R] == sum_(N, for_each=I)) <= sale(I, R, N)
(orders[R]  == len_(I))             <= sale(I, R, N)
(biggest[R] == max_(I, order_by=N)) <= sale(I, R, N)

print(sorted((revenue[R] == Z).data))
print(sorted((orders[R] == Z).data))
print(sorted((biggest[R] == Z).data))

# an aggregate fills Z like any table, so a gate may check it afterwards
on_target(R) <= (revenue[R] == Z) & (Z >= 100)
print(sorted(on_target(R).data))

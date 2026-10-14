from pyDatalog import pyDatalog

pyDatalog.create_terms('I, R, N, Z, sale, right, wrong')

# sale 6 has exactly the same amount as sale 1
for sid, region, amount in [(1, 'north', 50), (2, 'north', 70),
                            (3, 'south', 30), (4, 'south', 90),
                            (5, 'west', 60), (6, 'north', 50)]:
    +sale(sid, region, amount)

(right[R] == sum_(N, for_each=I)) <= sale(I, R, N)   # one per sale
(wrong[R] == sum_(N, for_each=N)) <= sale(I, R, N)   # one per amount
print(sorted((right[R] == Z).data))
print(sorted((wrong[R] == Z).data))

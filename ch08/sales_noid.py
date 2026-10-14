from pyDatalog import pyDatalog

pyDatalog.create_terms('R, N, Z, tally, revenue')

+tally('north', 50)
+tally('north', 70)
+tally('north', 50)              # the same card again

(revenue[R] == sum_(N, for_each=N)) <= tally(R, N)

print(len(tally(R, N).data))
print(sorted((revenue[R] == Z).data))

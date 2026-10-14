from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, tip, tip_c, total, total_c')

staff = [('ana', 'cafe', 1250.35), ('ben', 'cafe', 980.10),
         ('cy', 'bar', 1105.55)]

for name, place, amount in staff:
    +tip(name, place, amount)                      # floats
    +tip_c(name, place, round(amount * 100))       # whole cents

(total[Y] == sum_(N, for_each=X)) <= tip(X, Y, N)
(total_c[Y] == sum_(N, for_each=X)) <= tip_c(X, Y, N)
print(sorted((total[Y] == Z).data))
print(sorted((total_c[Y] == Z).data))

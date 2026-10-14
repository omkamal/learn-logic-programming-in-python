from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, pay, pay_c, total, total_c')

# the same five people, paid to the cent
staff = [('ann', 'eng', 1200.10), ('bob', 'eng', 1000.20),
         ('cid', 'ops', 800.35), ('dee', 'ops', 900.05),
         ('eli', 'hr', 700.15)]

for name, dept, dollars in staff:
    +pay(name, dept, dollars)                   # dollars, as floats
    +pay_c(name, dept, round(dollars * 100))    # the same pay in cents

(total[Y] == sum_(N, for_each=X)) <= pay(X, Y, N)
(total_c[Y] == sum_(N, for_each=X)) <= pay_c(X, Y, N)

def money(cents):                   # for people, only at the very end
    return '%d.%02d' % (cents // 100, cents % 100)

floats = dict((total[Y] == Z).data)
cents = dict((total_c[Y] == Z).data)
print('dept  floats               cents  for people')
for dept in sorted(cents):
    print('%-5s %-20r %6d  %s' % (dept, floats[dept], cents[dept],
                                  money(cents[dept])))

from pyDatalog import pyDatalog

pyDatalog.create_terms('seat, next_to, at_end, arrangement')
pyDatalog.create_terms('Ana, Ben, Cy, Dee, Eli')
pyDatalog.create_terms('fit1, fit2, fit3, fit4, fit5')

for s in range(5):                      # five chairs in a row, 0 to 4
    +seat(s)
for s in range(4):
    +next_to(s, s + 1)
    +next_to(s + 1, s)
+at_end(0)
+at_end(4)

# each variable holds the chair number of that guest
arrangement(Ana, Ben, Cy, Dee, Eli) <= (
    seat(Ana) & seat(Ben) & (Ben != Ana) &
    seat(Cy) & (Cy != Ana) & (Cy != Ben) &
    seat(Dee) & (Dee != Ana) & (Dee != Ben) & (Dee != Cy) &
    seat(Eli) & (Eli != Ana) & (Eli != Ben) & (Eli != Cy) & (Eli != Dee))

guests = (Ana, Ben, Cy, Dee, Eli)
fit1(*guests) <= arrangement(*guests) & ~next_to(Cy, Dee)
fit2(*guests) <= fit1(*guests) & at_end(Eli)
fit3(*guests) <= fit2(*guests) & (Ben < Dee)
fit4(*guests) <= fit3(*guests) & next_to(Cy, Eli)
fit5(*guests) <= fit4(*guests) & (Ana < Cy)

clues = [(arrangement, 'every guest in a different chair'),
         (fit1, 'Cy does not sit next to Dee'),
         (fit2, 'Eli sits at one end'),
         (fit3, 'Ben sits somewhere left of Dee'),
         (fit4, 'Cy sits next to Eli'),
         (fit5, 'Ana sits somewhere left of Cy')]
print('plans  clue added')
for rule, clue in clues:
    print('%5d  %s' % (len(rule(*guests).data), clue))

names = ['Ana', 'Ben', 'Cy', 'Dee', 'Eli']
plan = dict(zip(names, fit5(*guests).data[0]))
for name, chair in sorted(plan.items(), key=lambda pair: pair[1]):
    print('chair', chair, name)

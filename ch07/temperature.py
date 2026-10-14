from pyDatalog import pyDatalog

pyDatalog.create_terms('D, C, F, temp, fahrenheit, heat_warning, late')

for day, deg in [('mon', -10), ('tue', 0), ('wed', 5), ('thu', 20),
                 ('fri', 35)]:
    +temp(day, deg)

fahrenheit(D, F) <= temp(D, C) & (F == C * 9 // 5 + 32)
print(sorted(fahrenheit(D, F).data))

# calculate first, then check the result
heat_warning(D) <= temp(D, C) & (F == C * 9 // 5 + 32) & (F >= 95)
print(sorted(heat_warning(D).data))

# the check before the calculation: F is still blank
late(D) <= temp(D, C) & (F >= 95) & (F == C * 9 // 5 + 32)
try:
    print(sorted(late(D).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])

from pyDatalog import pyDatalog

pyDatalog.create_terms('D, C, F, temp, fahrenheit')

for day, deg in [('sat', 22), ('sun', -3)]:
    +temp(day, deg)

fahrenheit(D, F) <= temp(D, C) & (F == C * 9 // 5 + 32)
print(sorted(fahrenheit(D, F).data))
print(22 * 9 / 5 + 32, -3 * 9 / 5 + 32)

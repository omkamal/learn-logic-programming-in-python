from pyDatalog import pyDatalog

pyDatalog.create_terms('O, T, D, order, discount')
for oid, total in [('o1', 80), ('o2', 150), ('o3', 400), ('o4', 200)]:
    +order(oid, total)

discount(O, 0) <= order(O, T) & (T < 100)
discount(O, D) <= order(O, T) & (T >= 100) & (T < 200) & (D == T * 5 // 100)
discount(O, D) <= order(O, T) & (T >= 200) & (D == T * 10 // 100)

print(sorted(discount(O, D).data))

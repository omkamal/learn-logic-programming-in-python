from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, D, F, late, fee')
for m, b, d in [('mia', 'atlas', 3), ('noor', 'poems', 6),
                ('omar', 'maps', 2)]:
    +late(m, b, d)

fee(M, B, F) <= late(M, B, D) & (F == D * 25) & (F > 100)

+late('pia', 'maps', 4)          # 4 days: exactly 100 cents
+late('quin', 'atlas', 5)        # 5 days: 125 cents
print(sorted(fee(M, B, F).data))

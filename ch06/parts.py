from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, P, part, uses, unused, shared, exclusive')
for p in ['bolt', 'nut', 'washer', 'gear', 'spring', 'cable', 'clip']:
    +part(p)
for a, p in [('bike', 'bolt'), ('bike', 'nut'), ('bike', 'gear'),
             ('bike', 'cable'), ('lamp', 'bolt'), ('lamp', 'washer')]:
    +uses(a, p)

unused(P) <= part(P) & ~uses(A, P)           # no assembly uses P
shared(P) <= uses(A, P) & uses(B, P) & (A != B)
exclusive(A, P) <= uses(A, P) & ~shared(P)   # only A uses P

print(sorted(unused(P).data))
print(sorted(shared(P).data))
print(sorted(exclusive(A, P).data))

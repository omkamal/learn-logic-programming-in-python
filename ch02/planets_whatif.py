from pyDatalog import pyDatalog

pyDatalog.create_terms('P, M, N, position, has_moon')

+position('earth', 3)
+position('mars', 4)
+has_moon('mars', 'phobos')
+has_moon('mars', 'deimos')

print(sorted(has_moon('mars', M).data))
+has_moon('mars', 'deimos')           # the same card again
+has_moon('saturn', 'mimas')          # a planet with no position card
print(sorted(has_moon(P, M).data))
print(position(P, '3'))               # quoted: the text 3, not the number
print(position(P, 3))
print(position('saturn', N))

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent, position')
+parent('alice', 'bob')
+position('earth', 3)

print(sorted(parent('alice', X).data))
print(sorted(parent('Alice', X).data))       # capital A: another constant
print(sorted(position(X, 3).data))
print(sorted(position(X, '3').data))         # text 3 is not number 3

from pyDatalog import pyDatalog

pyDatalog.create_terms('I, F, num')

values = [0.5, 0.1, 100, 19.99, 2 ** 70]
for i, v in enumerate(values):
    +num(i, v)
back = dict(num(I, F).data)

for i, v in enumerate(values):
    print(repr(v), 'comes back unchanged:', back[i] == v)

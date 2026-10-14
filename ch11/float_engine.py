from pyDatalog import pyDatalog

def echo(v):                        # reports what it is given ...
    print('the function received', repr(v))
    return 0.1                      # ... and hands back an exact 0.1

pyDatalog.create_terms('I, F, N, T, num, tenth, back, echo')

values = [0.5, 100.25, 0.1, 0.2, 19.99, 12 * 0.14, 3.14159265358979,
          2 ** 70 + 1]
for i, v in enumerate(values):
    +num(i, v)                      # store each value as a fact ...
got = dict(num(I, F).data)          # ... and ask for it back

print('went in', 'came back', 'relative gap')
for i, v in enumerate(values):
    print(repr(v), repr(got[i]), '%.0e' % (abs(got[i] - v) / v))

# a function between a fact and an answer
+tenth(0.1)
back(T) <= tenth(N) & (T == echo(N))
print('the rule answered', back(T).data)

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, x, lives_in')
+lives_in('ann', 'paris')
+lives_in('bob', 'rome')

print(lives_in(x, 'paris').data)             # lowercase: no error, no rows
print(sorted(lives_in(X, 'paris').data))     # capital: a real blank

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, likes')
+likes('ann', 'tea')
+likes('bob', 'tea')
+likes('ann', 'jam')

print(sorted(likes('ann', X).data))
print(sorted(likes(X, 'tea').data))
print(bool(likes('bob', 'jam')))
print(len(likes(X, Y).data))

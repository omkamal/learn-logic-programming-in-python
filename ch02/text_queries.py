from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')

reply = pyDatalog.ask("parent('alice', X)")
print(sorted(reply.answers))
print(pyDatalog.ask("parent('alice', 'bob')").answers)
print(pyDatalog.ask("parent('dave', X)"))      # nobody matches

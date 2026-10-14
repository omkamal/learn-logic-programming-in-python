from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')

reply = pyDatalog.ask("parent('dave', X)")
print(reply)
rows = [] if reply is None else sorted(reply.answers)
print(rows)

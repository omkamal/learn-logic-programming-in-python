from pyDatalog import pyDatalog

pyDatalog.create_terms('parent')
+parent('alice', 'bob')

reply = pyDatalog.ask("parent('zed', X)")      # no card matches
print(reply)
try:
    print(reply.answers)
except Exception as err:
    print(type(err).__name__ + ':', err)

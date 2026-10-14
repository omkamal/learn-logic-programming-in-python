from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, T, member, works_with')

for person, team in [('ana', 'red'), ('ben', 'red'),
                     ('cy', 'blue'), ('dee', 'blue')]:
    +member(person, team)

works_with(X, Y) <= member(X, T) & member(Y, T) & (X != Y)

print(len(works_with(X, Y).data), 'pairs (expected 4)')
print(sorted(works_with('dee', Y).data), '(expected cy)')

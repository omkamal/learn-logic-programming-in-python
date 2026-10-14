from pyDatalog import pyDatalog

pyDatalog.create_terms('Who, Title, member, loan')

+member('mona')
+member('nabil')
+member('rania')
+loan('mona', 'Maps of Salt')
+loan('nabil', 'The Glass Orchard')


def check_out(person, title):
    pyDatalog.assert_fact('loan', person, title)


def give_back(person, title):
    pyDatalog.retract_fact('loan', person, title)


print(sorted(loan('mona', Title).data))
print(sorted(loan(Who, 'Maps of Salt').data))
print(bool(loan(Who, 'Quiet Engines')))
check_out('rania', 'Quiet Engines')
print(sorted(loan(Who, 'Quiet Engines').data))
give_back('mona', 'Maps of Salt')
print(sorted(loan(Who, Title).data))
print(sorted(member(Who).data))

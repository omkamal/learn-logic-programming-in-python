from pyDatalog import pyDatalog

pyDatalog.create_terms('Who, Title, loan')

+loan('mona', 'Maps of Salt')

pyDatalog.assert_fact('loan', 'nabil', 'Maps of Salt')   # same book!
print(sorted(loan(Who, 'Maps of Salt').data))
pyDatalog.retract_fact('loan', 'rania', 'Maps of Salt')   # never lent
print(sorted(loan(Who, 'Maps of Salt').data))

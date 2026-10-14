from pyDatalog import pyDatalog

pyDatalog.create_terms('City, Country, capital')

+capital('peru', 'lima')
+capital('south africa', 'pretoria')
+capital('south africa', 'cape town')
+capital('south africa', 'bloemfontein')

for question in ["capital('south africa', City)",
                 "capital(Country, 'cape town')"]:
    reply = pyDatalog.ask(question)
    print(question, '->', sorted(row[0] for row in reply.answers))

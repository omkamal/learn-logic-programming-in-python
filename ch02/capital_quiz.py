from pyDatalog import pyDatalog

pyDatalog.create_terms('City, Country, capital')

+capital('egypt', 'cairo')
+capital('france', 'paris')
+capital('japan', 'tokyo')
+capital('kenya', 'nairobi')
+capital('peru', 'lima')

quiz = ["capital('peru', City)",
        "capital(Country, 'nairobi')",
        "capital('atlantis', City)"]

for question in quiz:
    reply = pyDatalog.ask(question)
    if reply is None:
        print(question, '-> no card matches')
    else:
        print(question, '->', sorted(row[0] for row in reply.answers))

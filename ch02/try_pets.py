from pyDatalog import pyDatalog

pyDatalog.create_terms('P, K, Who, Year, pet, lives_with')

+pet('milo', 'cat')
+pet('rex', 'dog')
+pet('luna', 'cat')
+lives_with('milo', 'sara', 2021)
+lives_with('rex', 'tom', 2019)
+lives_with('luna', 'sara', 2023)

print(sorted(pet(P, 'cat').data))          # blank first
print(sorted(pet('rex', K).data))          # blank last
print(sorted(lives_with(P, 'sara', Year).data))    # two blanks
print(bool(lives_with('rex', 'sara', Year)))       # yes or no

for question in ["pet('luna', K)", "pet('zed', K)"]:
    reply = pyDatalog.ask(question)
    print(question, '->', 'no card' if reply is None else reply.answers)

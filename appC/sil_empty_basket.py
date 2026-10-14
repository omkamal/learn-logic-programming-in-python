from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, N, member, loan, loans, idle')
for m in ['mia', 'omar']:
    +member(m)
+loan('mia', 'atlas')
+loan('mia', 'birds')

(loans[M] == len_(B)) <= loan(M, B)
idle(M) <= member(M) & ~loan(M, B)

print(sorted((loans[M] == N).data))
print((loans['omar'] == N).data)           # no row, not a zero
print(sorted(idle(M).data))

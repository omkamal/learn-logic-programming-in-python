from pyDatalog import pyDatalog

pyDatalog.create_terms('V, S, W, Pt, patient_in, registered, closed')
pyDatalog.create_terms('cleared, banned, works_in, may_enter')

for patient, ward in [('rosa', 'maternity'), ('ken', 'icu'),
                      ('liv', 'general'), ('max', 'general')]:
    +patient_in(patient, ward)
for visitor, patient in [('vera', 'rosa'), ('will', 'ken'),
                         ('xena', 'liv'), ('xena', 'max'),
                         ('yuri', 'ken'), ('yuri', 'liv')]:
    +registered(visitor, patient)
+closed('icu')
+cleared('will', 'icu')
+banned('xena')
+works_in('nora', 'icu')
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & ~closed(W) & ~banned(V))
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & cleared(V, W) & ~banned(V))
may_enter(S, W) <= works_in(S, W)

-cleared('will', 'icu')
rows = may_enter('will', W).data
print('will may enter:', sorted(row[0] for row in rows))

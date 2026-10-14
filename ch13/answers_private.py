from pyDatalog import pyDatalog

pyDatalog.create_terms('V, S, W, Pt, patient_in, registered, closed')
pyDatalog.create_terms('cleared, banned, works_in, may_enter, private')

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
+private('liv')                 # liv wants no visitors at all

# the private check comes after registered(V, Pt) has filled in Pt
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & ~private(Pt) & ~closed(W) & ~banned(V))
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & ~private(Pt) & cleared(V, W) & ~banned(V))
may_enter(S, W) <= works_in(S, W)

for visitor, ward in sorted(may_enter(V, W).data):
    print(f'{visitor:5} may enter {ward}')

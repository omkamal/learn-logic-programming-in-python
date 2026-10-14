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
+closed('icu')              # the intensive care ward is closed to visitors
+cleared('will', 'icu')     # ...except visitors the ward has cleared
+banned('xena')             # a hospital-wide ban
+works_in('nora', 'icu')    # staff

# an ordinary visit: a registered visitor, an open ward, no ban
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & ~closed(W) & ~banned(V))
# the exception: a closed ward still admits cleared visitors
may_enter(V, W) <= (registered(V, Pt) & patient_in(Pt, W)
                    & cleared(V, W) & ~banned(V))
# staff may enter the ward they work in
may_enter(S, W) <= works_in(S, W)

for visitor, ward in sorted(may_enter(V, W).data):
    print(f'{visitor:5} may enter {ward}')
print('icu:  ', sorted(row[0] for row in may_enter(V, 'icu').data))
print('yuri: ', sorted(row[0] for row in may_enter('yuri', W).data))
print('xena: ', sorted(row[0] for row in may_enter('xena', W).data))
-banned('xena')
print('xena after the ban is lifted:',
      sorted(row[0] for row in may_enter('xena', W).data))

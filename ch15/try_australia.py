from pyDatalog import pyDatalog

pyDatalog.create_terms('color, paint, WA, NT, SA, Qld, NSW, Vic, Tas')

for c in ['teal', 'violet', 'amber']:
    +color(c)

paint(WA, NT, SA, Qld, NSW, Vic, Tas) <= (
    color(WA) & color(NT) & (WA != NT) &
    color(SA) & (WA != SA) & (NT != SA) &
    color(Qld) & (NT != Qld) & (SA != Qld) &
    color(NSW) & (SA != NSW) & (Qld != NSW) &
    color(Vic) & (SA != Vic) & (NSW != Vic) &
    color(Tas))

answers = paint(WA, NT, SA, Qld, NSW, Vic, Tas).data
print(len(answers), 'colorings with three colors')
print(sorted(answers)[0])

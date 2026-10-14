from pyDatalog import pyDatalog

pyDatalog.create_terms('color, paint, Hills, Lake, Forest, Desert, Coast')

for c in ['teal', 'violet', 'amber']:
    +color(c)

paint(Hills, Lake, Forest, Desert, Coast) <= (
    color(Hills) & color(Lake) & (Hills != Lake) &
    color(Forest) & (Hills != Forest) & (Lake != Forest) &
    color(Desert) & (Hills != Desert) & (Forest != Desert) &
    color(Coast) & (Coast != Hills) & (Coast != Desert))

print(len(paint(Hills, Lake, Forest, Desert, Coast).data), 'colorings')

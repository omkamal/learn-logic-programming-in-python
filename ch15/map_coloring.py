from pyDatalog import pyDatalog

pyDatalog.create_terms('color, paint, Hills, Lake, Forest, Desert')

for c in ['teal', 'violet', 'amber']:
    +color(c)

# one "different color" check for each of the five borders
paint(Hills, Lake, Forest, Desert) <= (
    color(Hills) & color(Lake) & (Hills != Lake) &
    color(Forest) & (Hills != Forest) & (Lake != Forest) &
    color(Desert) & (Hills != Desert) & (Forest != Desert))

answers = sorted(paint(Hills, Lake, Forest, Desert).data)
print(len(answers), 'colorings')
for row in answers:
    print(row)

# ask the same rule another way round: Hills must be teal
print(sorted(paint('teal', Lake, Forest, Desert).data))

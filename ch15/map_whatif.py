from pyDatalog import pyDatalog

pyDatalog.create_terms('color, paint, Hills, Lake, Forest, Desert')

for c in ['teal', 'violet', 'amber']:
    +color(c)

# the lake dries up: Lake and Desert now share a border (a sixth check)
paint(Hills, Lake, Forest, Desert) <= (
    color(Hills) & color(Lake) & (Hills != Lake) &
    color(Forest) & (Hills != Forest) & (Lake != Forest) &
    color(Desert) & (Hills != Desert) & (Forest != Desert) &
    (Lake != Desert))

print('three colors:', len(paint(Hills, Lake, Forest, Desert).data))
+color('slate')
print('four colors: ', len(paint(Hills, Lake, Forest, Desert).data))

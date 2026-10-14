from pyDatalog import pyDatalog

pyDatalog.create_terms('P, M, N, position, has_moon')

# position(planet, number counted from the sun)
+position('mercury', 1)
+position('venus', 2)
+position('earth', 3)
+position('mars', 4)
+position('jupiter', 5)

# has_moon(planet, moon): a few of the moons, not all of them
+has_moon('earth', 'moon')
+has_moon('mars', 'phobos')
+has_moon('mars', 'deimos')
+has_moon('jupiter', 'io')
+has_moon('jupiter', 'europa')
+has_moon('jupiter', 'ganymede')
+has_moon('jupiter', 'callisto')

print(sorted(has_moon('mars', M).data))
print(has_moon(P, 'europa'))
print(position(P, 3))
print(position('earth', N))
print(has_moon('venus', M))

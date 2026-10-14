# the bicycle in plain Python: a dictionary of dictionaries
HAS = {
    'bicycle': {'frame': 1, 'wheel': 2, 'handlebar': 1},
    'wheel': {'rim': 1, 'tire': 1, 'hub': 1, 'spoke': 32},
    'hub': {'axle': 1, 'bearing': 2},
    'frame': {'tube': 3, 'bolt': 4},
    'handlebar': {'grip': 2, 'bolt': 4},
}

def total_in(assembly):
    """{part: how many of it in ONE assembly}, at any depth."""
    found = {}
    for sub, how_many in HAS.get(assembly, {}).items():
        found[sub] = found.get(sub, 0) + how_many
        for part, count in total_in(sub).items():
            found[part] = found.get(part, 0) + how_many * count
    return found

print('spokes in a bicycle:', total_in('bicycle')['spoke'])
print('bolts in a bicycle: ', total_in('bicycle')['bolt'])

# the other questions each need their own function
def contains(assembly):
    return sorted(total_in(assembly))

def leaves():
    every = set(HAS) | {p for subs in HAS.values() for p in subs}
    return sorted(p for p in every if p not in HAS)

def where_used(part):          # asked "backwards": scan every assembly
    return sorted(a for a in HAS if part in total_in(a))

print('a wheel contains:', *contains('wheel'))
print('leaf parts:', *leaves())
print('bolts end up in:', *where_used('bolt'))

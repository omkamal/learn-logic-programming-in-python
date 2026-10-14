# the dependency questions in plain Python
NEEDS = {'shop': ['web', 'db'], 'web': ['http', 'templates'],
         'db': ['driver', 'pool'], 'http': ['sockets', 'tls'],
         'templates': ['strings'], 'tls': ['crypto'],
         'pool': ['threads'], 'report': ['db', 'strings']}

def requires(package):
    """Everything package needs, at any depth (no cycles allowed)."""
    found = set()
    for wanted in NEEDS.get(package, []):
        found.add(wanted)
        found |= requires(wanted)
    return found

print('to install shop:', len(requires('shop')), 'packages')

def breaks_if_removed(wanted):      # asked "backwards": scan everything
    return sorted(p for p in NEEDS if wanted in requires(p))

print('if tls is removed:', *breaks_if_removed('tls'))

# now the three slips from the logic version
for package, wanted in [('shop', 'auth'), ('auth', 'sessions'),
                        ('sessions', 'store'), ('store', 'auth')]:
    NEEDS.setdefault(package, []).append(wanted)

try:
    print(sorted(requires('shop')))
except RecursionError as error:
    print('RecursionError:', error)

# the repair: carry a "seen" set, a notebook written by hand
def requires_safe(package, seen=None):
    seen = set() if seen is None else seen
    for wanted in NEEDS.get(package, []):
        if wanted not in seen:
            seen.add(wanted)
            requires_safe(wanted, seen)
    return seen

print('to install shop:', len(requires_safe('shop')), 'packages')
print('in a cycle:', *sorted(p for p in NEEDS
                             if p in requires_safe(p)))

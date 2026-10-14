# the org chart in plain Python
SUB = {'engineering': 'acme', 'operations': 'acme',
       'platform': 'engineering', 'mobile': 'engineering',
       'web': 'engineering', 'research': 'engineering',
       'support': 'operations'}
MEMBERS = {'acme': ['ann'], 'engineering': ['jon'],
           'platform': ['bob', 'cid'], 'mobile': ['dee', 'eli'],
           'web': ['fay'], 'support': ['gus', 'hal', 'ivy']}

def people_in(team):
    found = set(MEMBERS.get(team, []))
    for child, parent in SUB.items():       # no way to ask "my children"
        if parent == team:
            found |= people_in(child)
    return found

all_teams = set(SUB) | set(SUB.values())
for team in sorted(all_teams):
    print(f'{team:12} {len(people_in(team)):2} people')
print('teams with nobody:', sorted(t for t in all_teams
                                   if not people_in(t)))

# the tempting shortcut, once dee also works for the web team
MEMBERS['web'].append('dee')

def head_count(team):            # add up the counts of the sub-teams
    n = len(MEMBERS.get(team, []))
    for child, parent in SUB.items():
        if parent == team:
            n += head_count(child)
    return n

print('engineering, adding counts:', head_count('engineering'))
print('engineering, merging sets: ', len(people_in('engineering')))

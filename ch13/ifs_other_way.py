# The same if-statement service, asked the other way round.
ROLE = {'maya': 'admin', 'noor': 'editor',
        'omar': 'viewer', 'pat': 'editor'}

def can(user, action):
    if action == 'read':
        return True
    if action == 'write' and ROLE[user] in ('admin', 'editor'):
        return True
    if action == 'delete' and ROLE[user] == 'admin':
        return True
    if user == 'pat' and action == 'write':
        return False  # pat's block, added later
    return False

# "Who can delete?" needs a brand-new function around can().
def who_can(action):
    return [user for user in ROLE if can(user, action)]

print('delete:', who_can('delete'))
print('write: ', who_can('write'))

# The usual repair: move pat's block above the rule that says yes.
def can_fixed(user, action):
    if user == 'pat' and action == 'write':
        return False
    return can(user, action)

print('write, repaired:', [u for u in ROLE if can_fixed(u, 'write')])

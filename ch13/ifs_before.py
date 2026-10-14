# The access check as it lives in one service today: four if-statements.
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

# Another team keeps the same policy in a spreadsheet.
SHEET = {('pat', 'write'): 'no'}

for user in ['maya', 'noor', 'omar', 'pat']:
    print(user, [a for a in ('read', 'write', 'delete') if can(user, a)])
print('spreadsheet: may pat write?', SHEET[('pat', 'write')])

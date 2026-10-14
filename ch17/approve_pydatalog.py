# Spending approvals: editors up to 1000, admins "no limit".
# House rule R: nobody may approve more than 5000.
from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, L, Amt, has_role, limit, approve')

+has_role('maya', 'admin')
+has_role('noor', 'editor')
+has_role('omar', 'viewer')
+limit('viewer', 0)
+limit('editor', 1000)

approve(U, Amt) <= has_role(U, R) & limit(R, L) & (Amt <= L)
approve(U, Amt) <= has_role(U, 'admin') & (Amt >= 0)    # admins: no limit

# Testing means choosing amounts. Which ones would YOU try?
for amount in (1000, 1001, 5000, 5001):
    print(amount, sorted(approve(U, amount).data))

# Asking "for which amounts?" is not allowed: a comparison checks values.
try:
    print(approve('maya', Amt))
except Exception as e:
    print(type(e).__name__, str(e).splitlines()[0])

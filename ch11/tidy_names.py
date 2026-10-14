from pyDatalog import pyDatalog

def tidy(text):
    """Strip stray spaces and line breaks, ignore capital letters."""
    return text.strip().lower()

pyDatalog.create_terms('N, R, typed, paid, both, signed, unpaid, tidy')

# the sign-up sheet was typed by hand; the payment list came from a bank
for r in ['  Ann ', 'BOB', 'cid\n', 'Dee']:
    +typed(r)
for n in ['ann', 'bob', 'cid']:
    +paid(n)

both(N) <= typed(N) & paid(N)               # raw spelling, no cleaning
signed(N) <= typed(R) & (N == tidy(R))      # clean each spelling first
unpaid(N) <= signed(N) & ~paid(N)

print('without cleaning:', sorted(both(N).data))
print('clean names:', sorted(signed(N).data))
print('unpaid:', sorted(unpaid(N).data))

+typed(' EVA ')                  # a new sign-up, typed carelessly
print('unpaid now:', sorted(unpaid(N).data))

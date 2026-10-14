from pyDatalog import pyDatalog

def vat_cents(cents):
    return round(cents * 14 / 100)

print('before create_terms:', vat_cents.__name__, vat_cents(300))

pyDatalog.create_terms('N, vat_cents')

print('after create_terms: ', vat_cents.__name__, vat_cents(300))
print('given a blank:', type(vat_cents(N)).__name__)

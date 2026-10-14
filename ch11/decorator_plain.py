def noisy(f):                       # takes a function ...
    def wrapper(x):                 # ... builds a new one around it ...
        print('calling', f.__name__, 'with', x)
        result = f(x)
        print('it returned', result)
        return result
    return wrapper                  # ... and hands the new one back

def vat_cents(cents):
    return round(cents * 14 / 100)

vat_cents = noisy(vat_cents)        # the name now means the wrapped one
print(vat_cents(300))

@noisy                              # the same thing, written shorter
def gross_cents(cents):
    return cents + round(cents * 14 / 100)

print(gross_cents(300))

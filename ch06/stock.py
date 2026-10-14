from pyDatalog import pyDatalog

pyDatalog.create_terms('P, W, product, warehouse, stock')
pyDatalog.create_terms('sold_out, short_in')
for p in ['kettle', 'lamp', 'mug', 'rug', 'vase']:
    +product(p)
for w in ['east', 'west']:
    +warehouse(w)
for p, w in [('kettle', 'east'), ('kettle', 'west'), ('lamp', 'east'),
             ('mug', 'west'), ('vase', 'east'), ('vase', 'west')]:
    +stock(p, w)

# W is blank and used only inside the ~ : "stocked ANYWHERE?"
sold_out(P) <= product(P) & ~stock(P, W)
# W is filled by warehouse(W) first : "stocked in THIS warehouse?"
short_in(P, W) <= product(P) & warehouse(W) & ~stock(P, W)

print(sorted(sold_out(P).data))
print(sorted(short_in(P, W).data))

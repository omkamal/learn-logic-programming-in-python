from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, R, page, links, orphan, visible, lost')
for p in ['home', 'about', 'blog', 'post1', 'post2', 'draft', 'notes']:
    +page(p)
for a, b in [('home', 'about'), ('home', 'blog'), ('blog', 'post1'),
             ('post1', 'post2'), ('post2', 'blog'), ('draft', 'notes')]:
    +links(a, b)

# 1. nobody links to the page (Q is blank on purpose)
orphan(P) <= page(P) & ~links(Q, P)

# 2. the page cannot be reached from home by following links
visible(P) <= links('home', P)
visible(P) <= visible(Q) & links(Q, P)       # recursive literal FIRST
lost(P) <= page(P) & (P != 'home') & ~visible(P)

print(sorted(orphan(P).data))
print(sorted(visible(P).data))
print(sorted(lost(P).data))

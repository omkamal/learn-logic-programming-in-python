from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, R, page, links, orphan, visible, lost')
for p in ['home', 'about', 'blog', 'post1', 'post2', 'draft', 'notes']:
    +page(p)
for a, b in [('home', 'about'), ('home', 'blog'), ('blog', 'post1'),
             ('post1', 'post2'), ('post2', 'blog'), ('draft', 'notes')]:
    +links(a, b)
orphan(P) <= page(P) & ~links(Q, P)
visible(P) <= links('home', P)
visible(P) <= visible(Q) & links(Q, P)
lost(P) <= page(P) & (P != 'home') & ~visible(P)

+links('home', 'draft')                # one new link, from the home page
print(sorted(orphan(P).data))
print(sorted(lost(P).data))

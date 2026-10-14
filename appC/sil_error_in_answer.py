from pyDatalog import pyDatalog

pyDatalog.create_terms('X, P, K, U, pack, unit')
+pack('box', 300, 1)
+pack('empty', 300, 0)             # a pack with no items

unit(X, U) <= pack(X, P, K) & (U == P / K)
for row in sorted((unit(X, U)).data, key=str):
    print(row)

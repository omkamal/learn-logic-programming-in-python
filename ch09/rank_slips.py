from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, R, emp, low_first, one_list, by_name')

+emp('ann', 'eng', 120)
+emp('bob', 'eng', 100)
+emp('cid', 'ops', 80)
+emp('dee', 'ops', 90)
+emp('eli', 'hr', 70)

# slip 1: the minus sign is missing, so each list runs low to high
(low_first[X] == rank_(group_by=Y, order_by=N)) <= emp(X, Y, N)
print(sorted((low_first[X] == R).data))

# slip 2: no group_by, so the whole company is one list
(one_list[X] == rank_(order_by=-N)) <= emp(X, Y, N)
print(sorted((one_list[X] == R).data))

# slip 3: a minus sign on the very variable in the brackets does nothing
(by_name[X] == rank_(group_by=Y, order_by=-X)) <= emp(X, Y, N)
print(sorted((by_name[X] == R).data))

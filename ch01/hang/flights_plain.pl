% The flights again, rules only (no questions): plain Prolog, no tabling.
flight(cai, dxb).
flight(dxb, lhr).
flight(lhr, cai).
flight(lhr, jfk).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

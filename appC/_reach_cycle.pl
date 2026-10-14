% A loop of three with no exit: the same reach/2, the same findall.
flight(cai, dxb).
flight(dxb, lhr).
flight(lhr, cai).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

:- findall(Y, reach(cai, Y), Ys), sort(Ys, Sorted), writeln(Sorted).

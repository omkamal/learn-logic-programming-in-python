% The same program, with one added line: :- table reach/2.
:- table reach/2.

flight(cai, dxb).
flight(dxb, lhr).
flight(lhr, cai).
flight(lhr, jfk).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

:- findall(Y, reach(cai, Y), Ys), sort(Ys, Sorted), writeln(Sorted).

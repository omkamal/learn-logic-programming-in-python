% The loop CAI -> DXB -> LHR -> CAI plus LHR -> JFK, right-recursive reach.
flight(cai, dxb).
flight(dxb, lhr).
flight(lhr, cai).
flight(lhr, jfk).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

:- findall(Y, reach(cai, Y), Ys), sort(Ys, Sorted), writeln(Sorted).

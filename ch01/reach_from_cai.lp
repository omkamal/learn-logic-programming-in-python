% The same program, showing only the cities that cai reaches.
flight(cai, dxb).  flight(dxb, lhr).
flight(lhr, cai).  flight(lhr, jfk).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

#show.
#show Y : reach(cai, Y).

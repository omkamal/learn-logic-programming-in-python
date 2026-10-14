% The flights, with the loop CAI -> DXB -> LHR -> CAI plus LHR -> JFK.
flight(cai, dxb).
flight(dxb, lhr).
flight(lhr, cai).
flight(lhr, jfk).

reach(X, Y) :- flight(X, Y).
reach(X, Y) :- flight(X, Z), reach(Z, Y).

% A yes/no question whose answer is yes.
:- ( reach(cai, jfk) -> writeln('cai to jfk: yes') ; writeln(no) ),
   flush_output.

% Now ask for ALL the cities that cai reaches.
:- findall(Y, reach(cai, Y), Ys), sort(Ys, Sorted), writeln(Sorted).

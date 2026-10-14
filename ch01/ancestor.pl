% A family tree in Prolog (SWI-Prolog 10). Facts, then two rules.
:- dynamic parent/2.          % parent facts may be added while it runs

parent(alice, bob).
parent(alice, carol).
parent(bob, dave).
parent(carol, erin).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Ask: whose ancestor is alice? Print one answer per line.
:- forall(ancestor(alice, Who), (write(Who), nl)).

% A yes/no question, and a question with the blank on the left.
:- ( ancestor(alice, erin) -> writeln(yes) ; writeln(no) ).
:- findall(A, ancestor(A, erin), As), writeln(As).

% A baby is born: add one fact and ask again.
:- assertz(parent(erin, fay)).
:- findall(D, ancestor(alice, D), Ds), sort(Ds, Sorted), writeln(Sorted).

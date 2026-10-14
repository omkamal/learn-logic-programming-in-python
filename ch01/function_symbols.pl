% Prolog terms can be nested: s(s(zero)) is a term inside a term.
% Two lines are enough to describe infinitely many facts.
nat(zero).
nat(s(N)) :- nat(N).

% Ask for the first five answers only; there is no last one.
:- forall(limit(5, nat(X)), (write(X), nl)).

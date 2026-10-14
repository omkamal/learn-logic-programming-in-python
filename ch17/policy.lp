% The access policy of Chapter 13, as an answer set program (clingo).
has_role(maya, admin).  has_role(noor, editor).
has_role(omar, viewer). has_role(pat, editor).
inherits(admin, editor). inherits(editor, viewer).
role_perm(viewer, read, report). role_perm(editor, write, report).
role_perm(admin, delete, report).
blocked(pat, write, report).

includes(R, R2) :- inherits(R, R2).
includes(R, R2) :- includes(R, P), inherits(P, R2).
can(U, P, Res) :- has_role(U, R), role_perm(R, P, Res),
                  not blocked(U, P, Res).
can(U, P, Res) :- has_role(U, R), includes(R, R2),
                  role_perm(R2, P, Res), not blocked(U, P, Res).
#show can/3.

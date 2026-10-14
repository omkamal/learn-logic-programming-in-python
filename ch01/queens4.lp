% 4 queens as a choice problem (clingo): one queen in each row, then
% forbid clashes. Every answer set is one placement.
n(1..4).
1 { queen(R, C) : n(C) } 1 :- n(R).          % choose a column for each row

:- queen(R1, C), queen(R2, C), R1 < R2.      % no two queens in a column
:- queen(R1, C1), queen(R2, C2), R1 < R2,    % none on a diagonal either
   |C1 - C2| == R2 - R1.

#show queen/2.

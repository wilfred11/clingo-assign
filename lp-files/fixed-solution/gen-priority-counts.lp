1 {steps(1..num_p)} num_p.

del(X, S) :- steps(S), S>0, priority(X,Y), column(X), Y = S.
priority_count(S, C) :- C=#count{X:del(X,S), column(X), steps(S)}, steps(S).

priority_number(S,K) :- priority_count(S,T), K= 1..T.


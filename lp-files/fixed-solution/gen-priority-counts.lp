1 {steps(1..NUM_P)} NUM_P :- num_p(NUM_P).

del(X, S) :- steps(S), S>0, priority(X,Y), column(X), Y = S.
priority_count(S, C) :- C=#count{X:del(X,S), column(X), steps(S)}, steps(S).

priority_number(S,K) :- priority_count(S,T), K= 1..T.


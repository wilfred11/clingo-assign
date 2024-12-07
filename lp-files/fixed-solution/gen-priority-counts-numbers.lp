NUM_P {step(1..NUM_P)} NUM_P :- num_p(NUM_P).

priority_count(S, C) :- C=#count{X:priority(X,S), column(X), step(S)}, step(S).

priority_number(S,K) :- priority_count(S,T), K= 1..T.


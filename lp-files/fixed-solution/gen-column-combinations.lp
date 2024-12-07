NUM_C {col_priority(X, S, K)  : priority(X,S), priority_count(S,C), K=1..C} NUM_C :- num_c(NUM_C).
:- col_priority(X1,S1,T1), col_priority(X,S,T), column(X), column(X1), X1=X,S=S, T1!=T.
:- col_priority(X1,S1,T1), col_priority(X,S,T), column(X), column(X1), X1!=X,S1=S, T1=T.


#show col_priority/3.
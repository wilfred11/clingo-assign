NUM_C {del_adv(X, S, K)  : del(X,S), priority_count(S,C), K=1..C} NUM_C :- num_c(NUM_C).
:- del_adv(X1,S1,T1), del_adv(X,S,T), column(X), column(X1), X1=X,S=S, T1!=T.
:- del_adv(X1,S1,T1), del_adv(X,S,T), column(X), column(X1), X1!=X,S1=S, T1=T.

#show del_adv/3.
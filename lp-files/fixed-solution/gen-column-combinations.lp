%1 {steps(0..num_p)} num_p.

%del(X, S) :- steps(S), S>0, priority(X,Y), column(X), Y = S.
%priority_count(S, C) :- C=#count{X:del(X,S), column(X), steps(S)}, steps(S).

num_c {del_adv(X, S, K)  : del(X,S), priority_count(S,C), K=1..C} num_c.
:- del_adv(X1,S1,T1), del_adv(X,S,T), column(X), column(X1), X1=X,S=S, T1!=T.
:- del_adv(X1,S1,T1), del_adv(X,S,T), column(X), column(X1), X1!=X,S1=S, T1=T.

%num_c {del_adv1(X,S,K,Z) : del_adv(X,S,K), Z=1..num_c} num_c.

%priority_number(S,K) :- priority_count(S,T), K= 1..T.

%#show steps/1.
#show del_adv/3.
%#hide priority_number/2.
%#hide priority_count/2.
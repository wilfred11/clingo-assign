queue(priority_number(X,Y),CN) :-  deletion_rank(priority_number(X,Y),CN),  CN<=S, del_c(S).
col_priority_comb(C,X,Y,V) :- queue(priority_number(X1,Y1),CN), comb(col_priority(C,X,Y),V), comb(V), column(C), X=X1, Y=Y1.

%count_combinations(COMB):- COMB= #count{Y:comb(X,Y)}.

hide_column(C,N) :- col_priority_comb(C,X,Y,N), comb(N).

:- k>N1, min(N1).

#minimize {X:del_c(X)}.

#show hide_column/2.
#show comb/1.
#show person/1.
#show p_religion_/2.
#show p_job_/2.
#show p_sex_/2.
#show p_married_status_/2.
#show val/1.
%#show count_ext_/5.
#show sum_test/1.
#show min/1.
#show del_c/1.
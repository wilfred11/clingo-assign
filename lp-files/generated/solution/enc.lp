queue(priority_number(X,Y),CN) :-  at(priority_number(X,Y),CN),  CN<=S, del_c(S).
del_adv1(C,X,Y,N) :- queue(priority_number(X1,Y1),CN), comb(del_adv(C,X,Y),N), comb(V), N=V, column(C), X=X1, Y=Y1.

count_combinations(COMB):- COMB= #count{Y:comb(X,Y)}.

hide_column(C,N) :- del_adv1(C,X,Y,N), comb(N).
%del_c {hide_column(C,N) :  del_adv1(C,X,Y,N), K=1..COMB, N=K, count_combinations(COMB)} del_c.

p_job_(X,na) :- p_job(X,J), hide_column(job,_).
p_religion_(X,na) :- p_religion(X,J), hide_column(religion,_).
p_married_status_(X,na) :- p_married_status(X,J), hide_column(married_status,_).
p_sex_(X,na) :- p_sex(X,J), hide_column(sex,_).

p_job_(X,J) :- p_job(X,J), not hide_column(job,_).
p_religion_(X,J) :- p_religion(X,J), not hide_column(religion,_).
p_married_status_(X,J) :- p_married_status(X,J), not hide_column(married_status,_).
p_sex_(X,J) :- p_sex(X,J), not hide_column(sex,_).

count_ext(J, R, M,S, N) :-  job(J), religion(R), married_status(M),sex(S), N= #count{X :p_job_(X,J), p_religion_(X,R), p_married_status_(X,M), p_sex_(X,S)}.
count_ext_(J, R, M,S, N) :- count_ext(J, R, M,S, N), N!=0.
sum_test(N1) :- N1= #sum{N,J,R,M,S : count_ext(J,R,M,S,N)}.
min(N1) :- N1= #min{N: count_ext_(J,R,M,S,N)}.
max(N1) :- N1= #max{N: count_ext_(J,R,M,S,N)}.

:- k>N1, min(N1).

#minimize {X:del_c(X)}.


%#show queue/2.
%#show del_adv1/4.
#show hide_column/2.
%#show count_combinations/1.
#show comb/1.
#show person/1.
#show p_religion_/2.
#show p_job_/2.
#show p_sex_/2.
#show p_married_status_/2.
#show val/1.
%#show count_ext_/5.
%#show sum_test/1.
#show min/1.
%#show max/1.
%#show problem/1.
#show del_c/1.

%#show comb/2.
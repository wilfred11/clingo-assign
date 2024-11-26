#const r = 4.
steps(0).

column(job).
column(religion).
column(married_status).
column(sex).


priority(job,1).
priority(religion,2).
priority(married_status,2).
priority(sex,3).

max_priority(N1,X) :-  column(X), #max{N:priority(X,N)}, steps(N1), N1>0.
not column(X) :- max_priority(N,X), column(X), steps(ST), ST>=N.
column_count(N1+N2) :- N1=#count{X:not column(X)}, N2=#count{X:column(X)}
columns_deleted(N) :- N=#count{X:not column(X)}.


p_job(X,_) :- p_job(X,J), not column(job).
p_religion(X,_) :- p_religion(X,J), not column(religion).
p_married_status(X,_) :- p_married_status(X,J), not column(married_status).
p_sex(X,_) :- p_sex(X,J), not column(sex).

count_ext(J, R, M,S, N) :- job(J), religion(R), married_status(M),sex(S), N= #count{X :p_job(X,J), p_religion(X,R), p_married_status(X,M), p_sex(X,S)}.
sum_test(N1) :- N1= #sum{N,J,R,M,S : count_ext(J,R,M,S,N)}.
min(N1) :- N1= #min{N: count_ext(J,R,M,S,N)}.

%:- min(N1), N1<k.
%not stop(N1).

#max{N1:max_priority(N1,X)}

steps(N3+1) :- , column_count(N2), steps(N3), N3<=N2, min(N1), not N1>=k.


not stop(N3) :- column_count(N2), steps(N3), N3<=N2.
stop(N3) :- column_count(N2), steps(N3), N3>N2, min(N1), N1>=k.

:- not stop(N3).
#show count_ext/5.
#show sum_test/1.
#show min/1.
#show stop/1.

%#const del_c=2.
%#const comb=1.
#const k=2.

del_c(1)|del_c(2)|del_c(3).
comb(1)|comb(2).


person(8101).
p_sex(8101,male).
p_married_status(8101,single).
p_job(8101,marketing_specialist).
p_religion(8101,islam).
person(13645).
p_sex(13645,female).
p_married_status(13645,single).
p_job(13645,graphic_designer).
p_religion(13645,hinduism).
person(26079).
p_sex(26079,female).
p_married_status(26079,widowed).
p_job(26079,accountant).
p_religion(26079,christianity).
person(16370).
p_sex(16370,female).
p_married_status(16370,divorced).
p_job(16370,project_manager).
p_religion(16370,hinduism).
person(22776).
p_sex(22776,male).
p_married_status(22776,divorced).
p_job(22776,marketing_specialist).
p_religion(22776,buddhism).
person(37559).
p_sex(37559,female).
p_married_status(37559,single).
p_job(37559,project_manager).
p_religion(37559,hinduism).
person(19084).
p_sex(19084,male).
p_married_status(19084,married).
p_job(19084,project_manager).
p_religion(19084,islam).
person(21580).
p_sex(21580,male).
p_married_status(21580,single).
p_job(21580,accountant).
p_religion(21580,christianity).
person(20720).
p_sex(20720,male).
p_married_status(20720,widowed).
p_job(20720,accountant).
p_religion(20720,islam).
person(41476).
p_sex(41476,female).
p_married_status(41476,widowed).
p_job(41476,software_engineer).
p_religion(41476,hinduism).
person(32687).
p_sex(32687,female).
p_married_status(32687,married).
p_job(32687,project_manager).
p_religion(32687,christianity).
person(21894).
p_sex(21894,female).
p_married_status(21894,married).
p_job(21894,marketing_specialist).
p_religion(21894,hinduism).
person(47676).
p_sex(47676,female).
p_married_status(47676,divorced).
p_job(47676,marketing_specialist).
p_religion(47676,buddhism).
person(37787).
p_sex(37787,male).
p_married_status(37787,widowed).
p_job(37787,software_engineer).
p_religion(37787,christianity).
person(15861).
p_sex(15861,male).
p_married_status(15861,married).
p_job(15861,accountant).
p_religion(15861,christianity).
person(172).
p_sex(172,male).
p_married_status(172,divorced).
p_job(172,software_engineer).
p_religion(172,hinduism).
person(23762).
p_sex(23762,female).
p_married_status(23762,widowed).
p_job(23762,software_engineer).
p_religion(23762,other).
person(36133).
p_sex(36133,male).
p_married_status(36133,married).
p_job(36133,project_manager).
p_religion(36133,christianity).
sex(male).
sex(female).
married_status(single).
married_status(widowed).
married_status(married).
married_status(divorced).
job(marketing_specialist).
job(software_engineer).
job(graphic_designer).
job(accountant).
job(project_manager).
religion(christianity).
religion(buddhism).
religion(other).
religion(islam).
religion(hinduism).

religion(na).
job(na).
married_status(na).
sex(na).


comb(del_adv(job,1,1),1).
comb(del_adv(religion,2,2),1).
comb(del_adv(married_status,2,1),1).
comb(del_adv(sex,3,1),1).

comb(del_adv(job,1,1),2).
comb(del_adv(religion,2,1),2).
comb(del_adv(married_status,2,2),2).
comb(del_adv(sex,3,1),2).

at(priority_number(1,1),1).
at(priority_number(2,1),2).
at(priority_number(2,2),3).
at(priority_number(3,1),4).


column(sex).
column(married_status).
column(job).
column(religion).


queue(priority_number(X,Y),CN) :-  at(priority_number(X,Y),CN),  CN<=S, del_c(S).
del_adv1(C,X,Y,N) :- queue(priority_number(X1,Y1),CN), comb(del_adv(C,X,Y),N), comb(V), N=V, column(C), X=X1, Y=Y1.

count_combinations(COMB):- COMB= #count{Y:comb(X,Y)}.

hide_column(C,N) :- del_adv1(C,X,Y,N), comb(N).
%del_c {hide_column(C,N) :  del_adv1(C,X,Y,N), K=1..COMB, N=K, count_combinations(COMB)} del_c.

val(na). 

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
 %#maximize [ hotel(X) : star(X,Y) = Y @ 1 ].
 %7 #minimize [ hotel(X) : cost(X,Y) : star(X,Z) = Y/Z @ 2 ]



#show queue/2.
#show del_adv1/4.
#show hide_column/2.
#show count_combinations/1.
#show comb/1.
%#show p_religion_/2.
%#show p_job_/2.
%#show p_sex_/2.
%#show p_married_status_/2.
#show count_ext_/5.
#show sum_test/1.
#show min/1.
#show max/1.
#show problem/1.
#show del_c/1.

%#show comb/2.
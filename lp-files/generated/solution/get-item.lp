person_(X) :- person(X), X=id.
p_sex_out(X, Y) :- p_sex_(X, Y), X=id.
p_married_status_out(X, Y) :- p_married_status_(X, Y), X=id.
p_religion_out(X, Y) :- p_religion_(X, Y), X=id.
p_job_out(X, Y) :- p_job_(X, Y), X=id.

#show p_sex_out/2.
#show p_job_out/2.
#show p_religion_out/2.
#show p_married_status_out/2.

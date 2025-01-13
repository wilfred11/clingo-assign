person_(X) :- person(X), X=id.
p_sex__(X, Y) :- p_sex_(X, Y), X=id.
p_married_status__(X, Y) :- p_married_status_(X, Y), X=id.
p_religion__(X, Y) :- p_religion_(X, Y), X=id.
p_job__(X, Y) :- p_job_(X, Y), X=id.
#show p_sex__/2.
#show p_job__/2.
#show p_religion__/2.
#show p_married_status__/2.

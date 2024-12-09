NUM_C {deletion_rank(priority_number(S,T), 1..NUM_C): priority_number(S,T)} NUM_C :- num_c(NUM_C).
% no same full priority numbers should have a different rank number
:- deletion_rank(priority_number(S,T),X), deletion_rank(priority_number(S,T),Y), X!=Y.
% priority numbers that have the same main priority number and a subpriority number only differing 1, should have a rank number that differs only 1.
:- deletion_rank(priority_number(S,T),X), deletion_rank(priority_number(S,T+1),Y), Y-X!=1.
% minimum rank should be 1
:- #min{X:deletion_rank(priority_number(_,_),X)}!=1.
% minimum main priority number should be 1
:- #min{X:deletion_rank(priority_number(X,_),_)}!=1.
% rank number 1 should only be given to a main priority number 1
:- deletion_rank(priority_number(S,_),1), S!=1.
% no two different main priority numbers can have the same rank number
:- deletion_rank(priority_number(S,_),X), deletion_rank(priority_number(S1,_),X), S!=S1.
% higher main priority number should have a rank number that is higher too
:- deletion_rank(priority_number(S,_),X), deletion_rank(priority_number(S1,_),X1), S>S1, X<X1.

#show deletion_rank/2.
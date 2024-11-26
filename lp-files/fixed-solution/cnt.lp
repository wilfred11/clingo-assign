priority_number(1,1).
priority_number(2,1).
priority_number(2,2).
priority_number(3,1).

priority_count(1,1).
priority_count(2,2).
priority_count(3,1).

4 {at(priority_number(S,T), 1..4): priority_number(S,T)} 4.
%{at(priority_number(S,T), 1..4): priority_number(S,T)} 4.
:- at(priority_number(S,T),X), at(priority_number(S,T),Y), X!=Y.
:- at(priority_number(S,T),X), at(priority_number(S,T+1),Y), Y-X!=1.
:- at(priority_number(S,_),X), at(priority_number(S1,_),X), S!=S1.
:- S1=#min{S:at(priority_number(S,T),X)}=1, #min{T:at(priority_number(S,T),X), S=S1}!=1.
:- #min{X:at(priority_number(_,_),X)}!=1.
:- #min{X:at(priority_number(X,_),_)}!=1.
:- at(priority_number(S,_),1), S!=1.
:- at(priority_number(S,_),X), at(priority_number(S1,_),X), S!=S1.
:- at(priority_number(S,_),X), at(priority_number(S1,_),X1), S>S1, X<X1.
:- at(priority_number(S,T),_), not at(priority_number(S,T-1),_), T!=1.
:- N=#count{X:at(priority_number(_,_),X)}, M= #max{X:at(priority_number(_,_),X)}, N!=M.
:- at(priority_number(S,_),X), at(priority_number(S1,_),X1), S1-S>=2, X1-X=1.
check_complete(F1) :- at(priority_number(F,_),X), at(priority_number(F1,T),Y), X>Y,F>F1.
:- check_complete(F1), priority_count(F1,C), M =#max{T:at(priority_number(F1,T),Y)}, C!=M.

%#show at/2.
%#show priority_number/2.
#show at/2.
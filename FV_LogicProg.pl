% Facts: defining parent relationships.
parent(john, mary).
parent(mary, susan).
parent(mary, david).
parent(susan, alice).

% Rule: defining ancestor relationships.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Query example:
% To find all ancestors of Alice, use:
% ?- ancestor(X, alice).
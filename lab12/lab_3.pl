witch(X) :- burns(X). % If she burns, she is a witch
burns(X) :- wood(X). % If she is wood, then she burns
wood(X) :- floats(X). % If she floats, the she is wood
floats(duck). % A duck floats
floats(X) :- sameWeight(X, Y), floats(Y). % She floats if she weighs the same as something that floats
sameWeight(woman, duck). % The woman weighs the same as the duck

% With the query ?- witch(woman).
% yields the result true

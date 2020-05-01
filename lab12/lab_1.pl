% i. 

killer(butch). % defines butch as a killer
married(mia, marsellus). % This makes mia married to marsellus
married(X,Y) :- married(Y,X). % This makes so that if you are married to someone, they are also married to you
dead(zed). % Defines zed as dead
kill(marsellus, Y) :- givesFootMassage(Y, mia). % If Y gives a foot massage to mia, then marsellus kills them
loves(mia, X) :- goodDancer(X). % If person X is a good dancer, then mia loves them
eats(jules, Z) :- nutritious(Z); tasty(Z). % If Z is either nutritious or tasty, jules eats it.


% ii.

hasWand(harry).
quidditchPlayer(harry).
wizard(ron).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

% 1. True, this comes from the line wizard(ron).
% 2. error, there is no witch definition
% 3. False, no one named hermione is defined as a wizard
% 4. error, there is no witch definition.
% 5. True, since harry is a quiddich player, he as a broom, and since he has a broom and a wand, he is a wizard.
% 6. ron. (if you run it again it says harry) Returns anyone who is a wizard
% 7. error, there is no witch definition.

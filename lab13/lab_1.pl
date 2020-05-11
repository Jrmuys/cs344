% Exercise 3.2

directlyin(irina, natasha).
directlyin(natasha, olga).
directlyin(olga,katarina).

in(X,Y) :- directlyin(X,Y).
in(X,Y) :- directlyin(X,Z),
    in(Z,Y).

% Excercise 4.5

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([G],[E]) :- tran(G,E).
listtran([A|TB],[C|TD]) :- listtran(TB, TD), 
    tran(A,C), tran(B,D).
    
% A generalized modus ponens only works for implications of horn clauses which is what prologue impliments, so the kind of logic
% that prolog impliments is based on modus ponsens, so yes, it can. Here is an example

breaths(X, air) :- human(X).
dieswithout(X,Y) :- human(X), breaths(X, Y).
human(joel).

% Here if you ask
% ?- dieswithout(joel, air).
% This utilizes the logical generalized modus ponens to derive that joel dies without air when it was not explicitly stated.

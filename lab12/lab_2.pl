% 2.1
% --------------------
% 1. Yes
% 2. No
% 8. Yes, X is instantiated to bread
% 9. Yes, Y is instantiated to bread, X is instantiated to sausage
% 14. No, since X can't be instantiated to both things

% 2.2
% -------------------

house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

% Produces "procedure `wizard(A)' does not exist" for all inputs. If you add a definition for wizard somewhere,
% then you get true for 'McGonagall' and hermione as inputs.


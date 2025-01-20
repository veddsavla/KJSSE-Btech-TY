female(savita).
female(saroj).
female(priya).
female(kinal).
female(rinkal).
female(payal).
female(hetal).
female(sonal).
female(ayushi).
female(ninjal).

male(kantilal).
male(premchand).
male(anup).
male(mitesh).
male(shail).
male(vivek).
male(milan).
male(jiten).
male(praag).
male(shaurya).
male(rian).
male(jenil).
male(harshay).
male(mahir).
male(vedansh).

father(kantilal, mitesh).
father(kantilal, milan).
father(kantilal, hetal).
father(premchand, priya).
father(premchand, kinal).
father(premchand, rinkal).
father(premchand, payal).
father(mitesh, vedansh).
father(milan, ninjal).
father(jiten, harshay).
father(jiten, mahir).
father(anup, jenil).
father(anup, ayushi).
father(shail, rian).
father(shail, shaurya).
father(vivek, praag).

mother(saroj, mitesh).
mother(saroj, milan).
mother(saroj, hetal).
mother(savita, priya).
mother(savita, kinal).
mother(savita, rinkal).
mother(savita, payal).
mother(kinal, vedansh).
mother(sonal, ninjal).
mother(hetal, harshay).
mother(hetal, mahir).
mother(priya, jenil).
mother(priya, ayushi).
mother(rinkal, rian).
mother(rinkal, shaurya).
mother(payal, praag).

parent(X, Y):- mother(X, Y); father(X, Y).
child(Y, X):- parent(X, Y).
grandparent(X, Y):- parent(X, Z), parent(Z, Y).
grandchild(Y, X):- grandparent(X, Y).
sibling(X, Y):- father(F, X), father(F, Y), mother(M, X), mother(M, Y), X\=Y.
cousin(X, Y):- parent(P1, X), parent(P2, Y), sibling(P1, P2), X\=Y.
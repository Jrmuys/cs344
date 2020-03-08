from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
])
print("Compute P(Raise | sunny)")
# Compute P(Raise | sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
print("Compute P(Raise | happy ∧ sunny)")
# Compute P(Raise | happy ∧ sunny)
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())

"""
Working them out, I got the same answers as the algorithms. The first answer can be read directly off of the
diagram because the probability of a raise is independent of the probability of whether it is sunny or not.

The second problem depends on the probability of whether it is sunny or not, so even though you know you are happy,
the fact that it is also sunny means that there is only a small increase in the chance you got a raise.
"""

print("Compute P(Raise | happy)")
# Compute P(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print("Compute P(Raise | happy ∧ ¬sunny)")
# Compute P(Raise | happy ∧ ¬sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

"""
The first answer does make sense that you would have an even greater chance of having gotten a raise knowing that you
are happy. This is because for P(Raise | happy ∧ sunny), it being sunny is a much more likely cause of happiness
and likely explains the state of happiness, whereas if you don't know it if is sunny, there is a greater chance
that it was getting a raise that made you happy, because it is very unlikely you get a raise AND it is sunny.

The last question makes sense because the fact that it is not sunny means something is likely causing your happiness
because the chance of you being happy if it is not sunny and you didn't get a raise is so low, that the chance you got
a raise is much higher than before (still not likely though because the prior probability of the getting a raise
is so low)
"""

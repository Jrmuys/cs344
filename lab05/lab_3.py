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

print("Compute P(Raise | happy)")
# Compute P(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print("Compute P(Raise | happy ∧ ¬sunny)")
# Compute P(Raise | happy ∧ ¬sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
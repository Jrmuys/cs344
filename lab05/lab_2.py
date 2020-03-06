from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2}),
])
print("Compute P(Cancer | positive results on both tests")
# Compute P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print("Compute P(Cancer | a positive result on test 1, but a negative result on test 2) ")
# Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

"""

These answers seem very different than I expected, the probability you have cancer even with two positive
tests is very low. This is because the prior probability of cancer is so exceedingly low that even with
two indications you have cancer, the probability you actually have cancer is still low. It is no surprise
give this that if one of those tests is negative, there is basically no chance you actually have cancer.

The value I got by enumerating by hand for part a:
    Probability you have cancer: 0.1698
    Probability you don't: 0.8302
    
for part b:
    Probability you have cancer: 0.00565
    Probability you don't: 0.99435
    
My hand calculated values match the values from the program.
"""
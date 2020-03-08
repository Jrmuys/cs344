'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
])
print("Compute P(Alarm | burglary ∧ ¬earthquake)")
# Compute P(Alarm | burglary ∧ ¬earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("Compute P(John | burglary ∧ ¬earthquake)")
# Compute P(John | burglary ∧ ¬earthquake)
print(enumeration_ask('John', dict(Burglary=T, Earthquake=T), burglary).show_approx())
print("Compute P(Burglary | alarm)")
# Compute P(Burglary | alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print("Compute P(Burglary | john ∧ mary)")
# Compute P(Burglary | john ∧ mary)
print(enumeration_ask('Burglary', dict(John=T, Mary=T), burglary).show_approx())

"""
These don't all match the exact inference algorithm because they are estimates. Rejection sampling is the worst
performing on this data set, which takes a bunch of samples of the space and gives an estimate on those. The more
samples taken the more accurate the response. 

The second best is likelihood weighting, this is a smarter version of rejection sampling because it only generates 
samples that are constant with the evidence in a certain problem. It is no surprise that this performs better than the 
rejection sampling method. 
The best performing approximate inference method is Gibbs sampling. This method keeps the evidence variables fixed and 
randomly wanders around the sample space.
This produces the most accurate results that are fairly close to the actual value of the problem.
"""

'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108;
P[T, T, F] = 0.012
P[F, T, T] = 0.072;
P[F, T, F] = 0.008
P[T, F, T] = 0.016;
P[T, F, F] = 0.064
P[F, F, T] = 0.144;
P[F, F, F] = 0.576

print("Showing Cavity problem:")
# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

'''
I computed the value of P( cavity | catch ) as 0.529412 by hand

The value I got from the aima implementation is 0.529, so the my answer and the aima implementation align.
'''

Q = JointProbDist(['Coint1', 'Coin2'])
H, T = True, False
Q[T, T] = 0.25
Q[T, H] = 0.25
Q[H, T] = 0.25
Q[H, H] = 0.25

print("Showing coin problem")
QC = enumerate_joint_ask('Coin2', {'Coin1': H}, Q)
print(QC.show_approx())

'''
This confirms that the probability is still 50/50 even when 1 coin has been thrown.

I can see why this would not be used because the number of variables greatly increases the amount of data needed to
compute the results.
'''

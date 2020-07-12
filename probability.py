#!/usr/bin/env python3


print("""The probability of seeing a plane in 3 minutes: 0.6. What a probability of seeing a plane in 1 minute?

We have two possible outcomes: to see a plane or not to see a plane. So to calculate probability of seeing at least one plane in 1 minute we should first calculate probability of not seeing a plane in 3 minutes by formula: Q = 1 - P(A). 1 means that probability of all possible outcomes is 100% (we will see a plane or not see a plane anyway).

The probability of not seeing a plane in 3 minutes is Q = q1 * q2 * q3 (q - probability of not seeing a plane in 1 minute). If we suppose that q1 = q2 = q3, we can calculate q: q = 3\u221aQ . Now, using previous formula we can calculate probability of seeing a plane in 1 minute: p = 1 - q.""")

PA = 0.6
print('P(A) = 0.6')

Q = 1 - PA
print('Q = 1 - P(A)')

q = pow(Q, 1 / 3)

print('q1 = q2 = q3 = 3\u221aQ')

p = 1 - q

print('p = 1 - q')

print('The probability of see a plane in one minute: ' + str(p))

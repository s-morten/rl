import numpy as np
from scipy import linalg

P = np.array([[0.0, 0.7, 0.3],[0.5, 0.0, 0.5],[0.0, 0.1, 0.9]])
R = np.array([[0, 1, 10], [0, 0, 1], [0, -1, 10]])

y = 0.9
r = (P*R).sum(axis=1)

x = np.eye(3) - y * P

bellman = (linalg.inv(x) * r).sum(axis = 1)

print(bellman)

# eye * y * P invertieren * expected reward

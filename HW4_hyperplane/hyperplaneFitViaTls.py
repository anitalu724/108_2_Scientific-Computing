import os
def hyperplaneFitViaTls(data):
    from numpy.linalg import eig
    import numpy as np
    n_dim, n = len(data), len(data[0])
    mean, s = [], 0
    for i in range(n_dim):
        s = sum(data[i])
        mean.append(s/n)
    for i in range(n_dim):
        for j in range(len(data[i])):
            data[i][j] = data[i][j] - mean[i]
    data = np.array(data)
    C = data.dot(data.transpose())
    v, w = eig(C)
    index = np.argmin(v)
    eigenVector = w[:, index]
    if eigenVector[0] < 0:
        eigenVector = -eigenVector
    b = -eigenVector.dot(mean)
    ans = np.append(eigenVector, b)
    return ans

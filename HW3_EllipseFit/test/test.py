# coding: utf-8

import numpy as np


from skimage.measure import EllipseModel


# Play around with sigma here, the larger the the better you notice the
# qualitiy difference between algebraic and geometric fit
SIGMA = 5


# t = np.linspace(0, 2 * np.pi, 100)
# a = 20
# b = 30
# xc = 20
# yc = 30
# x = xc + a * np.cos(t)
# y = yc + b * np.sin(t)
# data = np.column_stack([x, y])
# np.random.seed(seed=1234)
# data += SIGMA*np.random.normal(size=data.shape)


# Geometric fit
# model = EllipseModel()
# model.estimate(data)

# print (model._params)
# print (np.sum(model.residuals(data)))


# Algebraic fit (disregarding the constraint B^2−4AC for simplicity as it always
# converges to an ellipse here)

# Ax^2 + Bxy + Cy^2 + Dx + Ey + 1 = 0

def ellipseFit(data):
    A = np.zeros((len(data[0]), 5), dtype=np.double)
    for i in range(len(data[0])):
        A[i, 0] = data[0][i]**2
        A[i, 1] = data[0][i]*data[1][i]
        A[i, 2] = data[1][i]**2
        A[i, 3] = data[0][i]
        A[i, 4] = data[1][i]
    b = -np.ones((len(data[0]), ))


    A, B, C, D, E = np.linalg.lstsq(A, b)[0]

    # convert to parametric form
    M0 = np.array([
        1, D/2, E/2,
        D/2, A, B/2,
        E/2, B/2, C,
    ]).reshape(3, 3)
    M = np.array([
        A, B/2,
        B/2, C,
    ]).reshape(2, 2)
    l1, l2 = np.linalg.eigvals(M)
    xc = (B*E - 2*C*D)/(4*A*C - B**2)
    yc = (B*D - 2*A*E)/(4*A*C - B**2)
    a = np.sqrt(-np.linalg.det(M0)/np.linalg.det(M)/l1)
    b = np.sqrt(-np.linalg.det(M0)/np.linalg.det(M)/l2)
    theta = np.arctan(B/(A - C))/2

    return xc, yc, a, b

# model_alg = EllipseModel()
# model_alg._params = (xc, yc, a, b, theta)

# print (model_alg._params)
# # The sum of distances should usually be greater here than above
# print (np.sum(model_alg.residuals(data)))


# import pylab
# pylab.plot(data[:, 0], data[:, 1], '.r', label='Noisy data')
# pylab.plot(x, y, '.g', label='Original data')

# x, y = model.predict_xy(t)
# pylab.plot(x, y, '-b', label='Geometric fit')

# x, y = model_alg.predict_xy(t)
# pylab.plot(x, y, '-y', label='Algebraic fit')

# pylab.axis('equal')
# pylab.legend(loc='upper left')
# pylab.show()
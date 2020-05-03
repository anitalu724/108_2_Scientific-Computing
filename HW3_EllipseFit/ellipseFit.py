import numpy as np
from scipy import optimize
import os
import math

def ellipseFit(data):
    x_list, y_list = data[0], data[1]
    x_init, y_init = sum(x_list)/len(x_list), sum(y_list)/len(y_list)
    r1, r2 = sseOfEllipseFit([x_init, y_init], data)
    center0 = [x_init, y_init, r1, r2]
    # radius = [0,0]
    def f(center0):
        a, b, r1, r2 = center0[0], center0[1], center0[2], center0[3]
        
        ans = 0
        for i in range(len(data[0])):
            ans += (((data[0][i]-a)/r1)**2+((data[1][i]-b)/r2)**2-1)**2
        return ans

    center = optimize.fmin(f, center0, disp=False)
    return center[0],center[1],center[2],center[3],


def sseOfEllipseFit(center, data):
    x_h, y_k = [], []
    for i in range(len(data[0])):
        x_h.append((data[0][i]-center[0])**2)
        y_k.append((data[1][i]-center[1])**2)
    x_h = np.array(x_h)
    y_k = np.array(y_k)
    # X = x_h/y_k
    X = np.vstack([x_h, y_k]).T
    Y = np.ones(len(x_h)).T
    A, B = np.linalg.lstsq(X, Y)[0]
    r1 = 1/np.sqrt(A)
    r2 = 1/np.sqrt(B)
    # print(r1, r2)
    return r1, r2
    
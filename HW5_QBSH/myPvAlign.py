def myPvAlign(pv, noteVec):
    import numpy as np
    import os, sys
    INF = sys.maxsize
    matrix = np.zeros((len(noteVec),len(pv)))
    for i in range(len(noteVec)):
        for j in range(len(pv)):
            matrix[i, j] = abs(noteVec[i] - pv[j])
    new_matrix = np.zeros((len(noteVec),len(pv)))
    for i in range(len(noteVec)):
        for j in range(len(pv)):
            if i == 0 and j == 0:
                new_matrix[i, j] = matrix[i, j]
            elif i == 0:
                new_matrix[i, j] = new_matrix[i, j-1] + matrix[i, j]
            elif i != 0 and j < i:
                new_matrix[i, j] = INF
            else:
                new_matrix[i, j] = min(new_matrix[i, j-1] + matrix[i, j], new_matrix[i-1, j-1] + matrix[i, j])

    ans = min(new_matrix[:, len(pv)-1])
    return ans
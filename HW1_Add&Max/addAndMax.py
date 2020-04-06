def addAndMax(A,B):
    import numpy as np
    n1, n2 = np.size(A,1),  np.size(B,1)
    m1, m2 = np.size(A,0),  np.size(B,0)
    m, n = max(m1, m2), max(n1, n2)
    C = np.zeros((m,n))
    max_num = C[0][0]
    for i in range(m):
        for j in range(n):
            if i < m1 and i < m2 and j < n1 and j < n2:
                C[i][j] = (A[i][j] + B[i][j])
            elif i < m2 and j < n2 and (j >= n1 or i >= m1):
                C[i][j] = (B[i][j])
            elif i < m1 and j < n1 and (i >= m2 or j >= n2) :
                C[i][j] = A[i][j]
            else:
                C[i][j] = 0
            if max_num < C[i][j]:
                max_num = C[i][j]
    ans = max_num
    return ans
import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    M,N = A.shape
    T = np.zeros((N,M) , dtype = A.dtype)
    for i in range(M):
        for j in range(N):
            T[j,i] = A[i,j]
    return T

    pass

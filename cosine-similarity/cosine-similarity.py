import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a  = np.asarray(a ,dtype = float)
    b = np.asarray (b , dtype = float)
    a_  = np.linalg.norm(a)
    b_ = np.linalg.norm(b)
    if a_ == 0 or b_ == 0:
        return 0.0
    return float(np.dot(a,b)/(a_*b_))

    pass
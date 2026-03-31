import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    sim = (np.dot(x1,x2))/((np.linalg.norm(x1))*(np.linalg.norm(x2)))
    if label == 1:
        l = 1-sim
    else:
        l = max(0,sim-margin)
    return l
    
    
    
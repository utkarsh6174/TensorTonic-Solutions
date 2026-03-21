import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    _, count = np.unique(y,return_counts = True)
    probs = count/count.sum()
    probs = probs[probs>0]
    return  -np.sum(probs*np.log2(probs))
    pass
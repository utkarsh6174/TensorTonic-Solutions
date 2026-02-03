import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x , dtype = float)
    p = np.asarray(p , dtype = float)
    if x.shape != p.shape:
        raise ValueError('shape doesnt match')
    if not np.allclose(sum(p) , 1.0 , atol=1e-6):
        raise ValueError("probabilites not sum up to 1")
    
    
    sums = np.sum(x*p)
    return float(sums)
    pass

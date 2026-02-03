import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    mean_x = np.mean(x)
    n = x.shape[0]
    var = np.sum((x-mean_x)**2)/(n-1)
    std = np.sqrt(var)
    return var , std

    pass
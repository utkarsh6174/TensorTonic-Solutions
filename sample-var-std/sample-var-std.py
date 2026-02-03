import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    mean_x = np.mean(x)
    n = x.shape[0]
    sum = 0
    for i in range(n):
        sum += (x[i] -mean_x)**2

    var = (1/(n-1))*sum
    std = np.sqrt(var)
    return var , std

    pass
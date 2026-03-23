import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x  = np.asarray(x)
    xmean = np.mean(x)
    n = len(x)
    sd = np.sqrt((1/(n-1))*np.sum((x-xmean)**2))
    t = (xmean - mu0 )/(sd/np.sqrt(n))
    return t
    pass
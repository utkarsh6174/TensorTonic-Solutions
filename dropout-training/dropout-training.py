import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x  = np.asarray(x)
    if not (0.0 <= p < 1.0):
        raise ValueError("P must be in [0,1]")

    if rng is None:
        random_vals = np.random.random(x.shape)
    else:
        random_vals = rng.random(x.shape)
    keep_mask = random_vals < 1-p 
    scale = 1.0/(1-p) if p < 1.0 else 0.0
    dropout_pattern = keep_mask.astype(x.dtype) * scale 
    output = x* dropout_pattern
    return output , dropout_pattern
    # Write code here
    pass
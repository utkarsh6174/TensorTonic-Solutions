import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.asarray(predictions)
    T,N = predictions.shape
    result = []
    for i in range(N):
        votes = predictions[:,i]
        counts = np.bincount(votes)
        result.append(np.argmax(counts))
    return result
    
import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points = np.asarray(points , dtype = float)
    assignments = np.asarray(assignments)
    n_features = points.shape[1]
    centroids = np.zeros((k,n_features))
    for j in range(k):
        cluster_points = points[assignments == j]
        if len(cluster_points) > 0:
            centroids[j] = cluster_points.mean(axis = 0)

    return centroids.tolist()
    
    
    
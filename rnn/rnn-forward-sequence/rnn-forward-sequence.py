import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    batch_size , time_steps , _ = X.shape
    hidden_states = []

    h_t = h_0
    for t in range(time_steps):
        x_t = X[:,t,:]

        h_t = np.tanh(
            x_t @ W_xh.T + 
            h_t @ W_hh.T +
            b_h
        )
        hidden_states.append(h_t)

    h_all = np.stack(hidden_states , axis = 1)
    h_final = h_t
    return h_all , h_final
        
    
    pass
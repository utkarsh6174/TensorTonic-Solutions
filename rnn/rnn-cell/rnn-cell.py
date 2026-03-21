import numpy as np

def rnn_cell(x_t: np.ndarray, h_prev: np.ndarray, 
             W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Single RNN cell forward pass.
    """
    # YOUR CODE HERE
    input_part = x_t @ W_xh.T
    hidden_part = h_prev @ W_hh.T

    h_t_linear = input_part+hidden_part + b_h

    h_t = np.tanh(h_t_linear)
    return h_t
    pass
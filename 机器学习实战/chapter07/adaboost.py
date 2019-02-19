import numpy as np


def load_simple_data():
    dat_mat = np.matrix([[1., 2.1],
                         [1.5, 1.6],
                         [1.3, 1.],
                         [1., 1.],
                         [2., 1.]])
    class_labels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dat_mat, class_labels

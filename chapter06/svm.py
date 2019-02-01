import numpy as np


def load_dataset(file_name):
    data_mat = []
    label_mat = []
    with open(file_name, 'r') as fr:
        for line in fr.readlines():
            line_arr = line.strip().split('\t')
            data_mat.append([float(line_arr[0]), float(line_arr[1])])
            label_mat.append(int(line_arr[2]))
        return data_mat, label_mat


def select_jrand(i, m):
    j = i
    while j == i:
        j = int(np.random.uniform(o, m))
    return j


def clip_alpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

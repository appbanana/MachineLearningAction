import logRegres
import numpy as np


def stoc_grad_ascent0(data_matrix, class_label):
    """
    随机梯度
    这个算法不太好 至少误判了三分之一的数据
    :param data_matrix:
    :param class_label:
    :return:
    """
    m, n = data_matrix.shape
    # 步长
    alpha = 0.01
    # 初始化所有的回归系数为1
    weights = np.ones(n)
    for i in range(m):
        # 先每一个样本与对应回归系数weights相乘 再求和 最后在带入sigmoid求值
        h = logRegres.sigmoid(np.sum(data_matrix[i] * weights))
        # 绝对误差
        error = class_label[i] - h
        # 修正误差
        weights = weights + alpha * error * data_matrix[i]
    return weights


def stoc_grad_ascent1(data_matrix, class_label, max_iter=150):
    """
    改进版随机梯度
    :param data_matrix:
    :param class_label:
    :return:
    """
    m, n = data_matrix.shape
    # 初始化所有的回归系数为1
    weights = np.ones(n)
    for j in range(max_iter):
        data_index = list(range(m))
        for i in range(m):
            # 步长
            alpha = 4 / (1.0 + j + i) + 0.01
            rand_index = int(np.random.uniform(0, len(data_index)))
            # 先每一个样本与对应回归系数weights相乘 再求和 最后在带入sigmoid求值
            h = logRegres.sigmoid(np.sum(data_matrix[rand_index] * weights))
            # 绝对误差
            error = class_label[rand_index] - h
            # 修正误差
            weights = weights + alpha * error * data_matrix[rand_index]
            del data_index[rand_index]
    return weights


if __name__ == '__main__':
    data_mat, label_mat = logRegres.load_dataset()

    # result = stoc_grad_ascent0(np.array(data_mat), label_mat)
    result = stoc_grad_ascent1(np.array(data_mat), label_mat, max_iter=500)
    print(result)

    result = logRegres.plot_best_fit(result)

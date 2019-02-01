import numpy as np


def load_dataset():
    """
    样本数据集
    :return: 返回数据和标签
    """
    data_mat = []
    label_mat = []
    with open('./data/testSet.txt', 'r') as fr:
        for line in fr.readlines():
            line_arr = line.strip().split()
            data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
            label_mat.append(int(line_arr[2]))
        return data_mat, label_mat


def sigmoid(input_x):
    """
    sigmoid 函数
    :param input_x:
    :return:
    """
    return 1.0 / (1 + np.exp(-input_x))


def grad_ascent(data_mat, class_labels):
    """
    计算梯度 返回最佳回归系数
    :param data_mat: 输入的特征向量矩阵
    :param class_labels: 标签矩阵
    :return:
    """
    data_matrix = np.mat(data_mat)
    # 将标签进行转置 行向量转化为列向量
    label_matrix = np.mat(class_labels).transpose()
    m, n = data_matrix.shape
    # 步长
    alpha = 0.001
    max_cycles = 500
    weights = np.ones((n, 1))
    for k in range(max_cycles):
        h = sigmoid(data_matrix * weights)
        error = (label_matrix - h)
        weights = weights + alpha * data_matrix.transpose() * error
    return weights


def plot_best_fit(weight):
    """
    画出回归最佳拟合直线
    :param weight:
    :return:
    """
    import matplotlib.pyplot as plt
    data_mat, label_mat = load_dataset()
    data_arr = np.array(data_mat)
    if hasattr(weight, 'getA'):
        weight = weight.getA()

    n = data_arr.shape[0]
    xcord1, ycord1 = [], []
    xcord2, ycord2 = [], []
    for i in range(n):
        if int(label_mat[i]) == 1:
            # 第一个特征当x横坐标
            xcord1.append(data_arr[i, 1])
            # 第二个特征当纵坐标
            ycord1.append(data_arr[i, 2])
        else:
            xcord2.append(data_arr[i, 1])
            ycord2.append(data_arr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, c='red', s=30, marker='^')
    ax.scatter(xcord2, ycord2, c='green', s=30)
    x = np.arange(-4, 4, 0.1)
    # 0 = w0 * x0 + w1 * x1 + w2 * x2 一直w， x1 求x2 x2 = -(w0 * x0 + w1 * x1) / w2
    y = -(weight[0] + weight[1] * x) / weight[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.savefig('{0}.png'.format('./img/Figure_02_2'))
    plt.show()


def stoc_grad_ascent1(data_matrix, class_label, max_iter=150):
    """
    改进版随机梯度
    :param data_matrix:
    :param class_label:
    :return: 返回回归系数
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
            h = sigmoid(np.sum(data_matrix[rand_index] * weights))
            # 绝对误差
            error = class_label[rand_index] - h
            # 修正误差
            weights = weights + alpha * error * data_matrix[rand_index]
            del data_index[rand_index]
    return weights


def classify_vector(inX, weights):
    """
    分类
    :param inX: 待测数据
    :param weights: 回归系数
    :return: 返回类型标签
    """
    #
    prob = sigmoid(np.sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

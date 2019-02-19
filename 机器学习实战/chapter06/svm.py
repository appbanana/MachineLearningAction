import numpy as np


def load_dataset(file_name):
    """
    加载数据
    :param file_name: 文件名称
    :return: 返回特征数据和标签数据
    """
    data_mat = []
    label_mat = []
    with open(file_name, 'r') as fr:
        for line in fr.readlines():
            line_arr = line.strip().split('\t')
            data_mat.append([float(line_arr[0]), float(line_arr[1])])
            label_mat.append(int(line_arr[2]))
        return data_mat, label_mat


def select_j_rand(i, m):
    """
    随机选择一个与i不同的j下标
    :param i: 输入的i小标
    :param m: alphas的数据长度
    :return: 返回j下标
    """
    j = i
    # 随机选择一个下标不为i的alpha值的下标
    while j == i:
        j = int(np.random.uniform(0, m))
    return j


def clip_alpha(aj, H, L):
    """
    调整alpha的取值，使其大于L 小于H
    :param aj: 数据的alpha值
    :param H: alpha的上限
    :param L: alpha的下限
    :return: 返回修正过的alpha
    """
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smo_simple(data_input, class_labels, C, toler, max_iter):
    """
    简化版smo算法
    :param data_input: 输入的特征数据
    :param class_labels: 输入的标签数据
    :param C: 惩罚因子
    :param toler: 容错率
    :param max_iter: 最大遍历数
    :return:
    """
    # 将输入的data_input，class_labels转化为向量
    data_mat = np.mat(data_input)
    # 将输入的class_labels转化为向量 在转置一下
    label_mat = np.mat(class_labels).transpose()
    # 初始化b的参数
    b = 0
    # data_mat.shape  (100, 2) m = 100 n = 2
    m, n = np.shape(data_mat)
    # 初始化100个1维0的数据
    alphas = np.mat(np.zeros((m, 1)))
    iter_num = 0
    # 最多迭代max_iter次
    while iter_num < max_iter:
        alpha_pairs_changed = 0
        for i in range(m):
            # 参考链接 https://blog.csdn.net/c406495762/article/details/78072313
            # 预测类别 参考上面u的函数 u = ∑ αi*yi*xi的转置 * x + b
            # np.multiply(alphas, label_mat).T 是1x100维数据，(data_mat * data_mat[i, :].T)是100x1维的数据，在相乘结果是1x1维的数据
            fxi = float(np.multiply(alphas, label_mat).T * (data_mat * data_mat[i, :].T)) + b
            #  基于预测结果和真实结果对比，计算误差
            ei = fxi - float(label_mat[i])
            # 如果不满足KKT条件 需要对alpha进行优化更新
            if (label_mat[i] * ei < -toler and (alphas[i] < C)) or (label_mat[i] * ei > toler and alphas[i] > 0):
                # 随机选择另一个与alpha_i成对优化的alpha_j
                j = select_j_rand(i, m)
                # 再次预测fxj
                fxj = float(np.multiply(alphas, label_mat).T * (data_mat * data_mat[j, :].T)) + b
                # 第一步：计算误差Ej
                ej = fxj - float(label_mat[j])
                alpha_iold = alphas[i].copy()
                alpha_jold = alphas[j].copy()
                # α1(new)y1 + α2(new)y2 = α1(old)y1 + α2(old)y2 = C
                # 第二步 计算上下界H和L
                if label_mat[i] != label_mat[j]:
                    # 当y1和y2 不相等时 一个为1 一个为-1
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    # 当y1和y2 相等时 同时为1或者同时为-1
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print('L == H')
                    continue
                # eta  为学习速录
                # 第三步：计算学习率 η
                eta = 2.0 * data_mat[i, :] * data_mat[j, :].T - data_mat[i, :] * data_mat[i, :].T \
                      - data_mat[j, :] * data_mat[j, :].T
                if eta > 0:
                    continue
                # 第四步：更新αj
                alphas[j] -= label_mat[j] * (ei - ej) / eta
                # 第五步：修剪αj
                alphas[j] = clip_alpha(alphas[j], H, L)
                if abs(alphas[j] - alpha_jold) < 0.00001:
                    print('j not moving enough')
                    continue
                # 第6步：更新αi
                alphas[i] += label_mat[j] * label_mat[i] * (alpha_jold - alphas[j])
                # 第7步：更新b1，b2
                b1 = b - ei - label_mat[i] * (alphas[i] - alpha_iold) * data_mat[i, :] * data_mat[i, :].T \
                     - label_mat[j] * (alphas[j] - alpha_jold) * data_mat[i, :] * data_mat[j, :].T
                b2 = b - ej - label_mat[i] * (alphas[i] - alpha_iold) * data_mat[i, :] * data_mat[j, :].T \
                     - label_mat[j] * (alphas[j] - alpha_jold) * data_mat[j, :] * data_mat[j, :].T
                # 第8步：根据b1和b2 更新b
                if (alphas[i] > 0) and (alphas[i] < C):
                    b = b1
                elif (alphas[j] > 0) and (alphas[j] < C):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alpha_pairs_changed += 1
                print("iter: %d i:%d, pairs changed %d" % (iter_num, i, alpha_pairs_changed))
        if alpha_pairs_changed == 0:
            iter_num += 1
        else:
            iter_num = 0
        print("iteration number: %d" % iter_num)
    return b, alphas


def get_w(data_mat, label_mat, alphas):
    """
    计算w向量
    :param data_mat: 特征向量
    :param label_mat: 标签数据
    :param alphas: 由smo算法计算出来的alphas
    :return: 返回w向量 也就是超平面的法向量
    """
    alphas, data_mat, label_mat = np.array(alphas), np.array(data_mat), np.array(label_mat)
    # np.tile(label_mat.reshape(1, -1).T, (1, 2)) * data_mat).shape (100, 2)
    # 此时w向量是一个2x1维的向量
    w = np.dot((np.tile(label_mat.reshape(1, -1).T, (1, 2)) * data_mat).T, alphas)
    # 转化为数组后在返回
    return w.tolist()
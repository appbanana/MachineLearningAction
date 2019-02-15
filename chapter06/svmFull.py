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


class OptStruct:
    """
    此对象主要是为了作为一个数据结构来使用，方便存储值 传值
    """

    def __init__(self, data_mat, class_labels, C, toler):
        self.X = data_mat  # 特征矩阵
        self.label_mat = class_labels  # 标签矩阵
        self.C = C  # 松弛变量 惩罚因子
        self.tol = toler  # 容错率
        self.m = np.shape(data_mat)[0]  # 数据矩阵行数 数据的长度
        # 矩阵行数初始化为0的alpha参数
        self.alphas = np.mat(np.zeros((self.m, 1)))
        self.b = 0
        # 根据矩阵行数初始化化误差缓存，第一列为是否有效的标志位，第二列为实际的误差E的值。
        self.e_cache = np.mat(np.zeros((self.m, 2)))


def calc_ek(os, k):
    """
    计算误差
    :param os: OptStruct的一个实例对象
    :param k: 下标
    :return: 返回误差
    """
    fxk = float(np.multiply(os.alphas, os.label_mat).T * (os.X * os.X[k, :].T)) + os.b
    ek = fxk - float(os.label_mat[k])
    return ek


def select_j(i, os, ei):
    """
    改进后 选择第二个α的下标j
    :param i: 第一个α的下标i
    :param os: OptStruct的一个实例对象
    :param ei: 第一个αi的误差
    :return: 返回αj - αi最大的j下标和ej
    """
    max_k = -1
    max_delta_e = 0
    ej = 0
    os.e_cache[i] = [1, ei]
    # os.e_cache是一个矩阵 os.e_cache[:, 0].A 将矩阵转化为数组
    valid_e_cache_list = np.nonzero(os.e_cache[:, 0].A)[0]
    if len(valid_e_cache_list) > 1:
        for k in valid_e_cache_list:
            if k == i:
                continue
            ek = calc_ek(os, k)
            delta_e = np.abs(ei - ek)
            if delta_e > max_delta_e:
                # 选择使得ei-ek最大的α值
                max_k = k
                max_delta_e = delta_e
                ej = ek
        # 返回ei-ej最大的α的索引和ej
        return max_k, ej
    else:
        j = select_j_rand(i, os.m)
        ej = calc_ek(os, j)
    return j, ej


def update_ek(os, k):
    ek = calc_ek(os, k)
    os.e_cache[k] = [1, ek]


def innerL(i, os):
    """
    跟简化版的SMO算法函数差不多 只是做了优化
    :param i: 第一个α的下标i
    :param os: OptStruct的一个实例对象
    :return:
    """
    # 计算误差
    ei = calc_ek(os, i)
    # 不满足KKT条件 对alpha进行优化更新
    if ((os.label_mat[i] * ei < -os.tol) and (os.alphas[i] < os.C)) or (
            os.label_mat[i] * ei > os.tol and os.alphas[i] > 0):
        # 第一步：计算误差 启发式方法选择
        j, ej = select_j(i, os, ei)
        # 暂时保存αi和αj 用于计算更新新的αi，αj
        alpha_i_old = os.alphas[i].copy()
        alpha_j_old = os.alphas[j].copy()
        # 第二步：计算上下边界
        if os.label_mat[i] != os.label_mat[j]:
            # yi和yj标签异号
            L = max(0, os.alphas[j] - os.alphas[i])
            H = min(os.C, os.C + os.alphas[j] - os.alphas[i])
        else:
            # yi和yj同号
            L = max(0, os.alphas[j] + os.alphas[i] - os.C)
            H = min(os.C, os.alphas[j] + os.alphas[i])
        if L == H:
            return 0
        # 第三步：计算学习率 eta(η)
        eta = 2 * os.X[i, :] * os.X[j, :].T - os.X[i, :] * os.X[i, :].T - os.X[j, :] * os.X[j, :].T
        if eta >= 0:
            print('%f 大于0' % eta)
            return 0
        # 第四步：更新αj
        os.alphas[j] -= os.label_mat[j] * (ei - ej) / eta
        # 第五步：修改αj，使αj位于上下边界内
        os.alphas[j] = clip_alpha(os.alphas[j], H, L)
        update_ek(os, j)
        if np.abs(os.alphas[j] - alpha_j_old) < 0.00001:
            print('j not moving enough')
            return 0
        # 第六步：更新αi
        os.alphas[i] += os.label_mat[i] * os.label_mat[j] * (alpha_j_old - os.alphas[j])
        update_ek(os, i)
        # 第七步：计算b1， b2
        b1 = os.b - ei - os.label_mat[i] * (os.alphas[i] - alpha_i_old) * os.X[i, :] * os.X[i, :].T - os.label_mat[j] * (
                    os.alphas[j] - alpha_j_old) * os.X[i, :] * os.X[j, :].T
        b2 = os.b - ej - os.label_mat[i] * (os.alphas[i] - alpha_i_old) * os.X[i, :] * os.X[j, :].T - os.label_mat[j] * (
                    os.alphas[j] - alpha_j_old) * os.X[j, :] * os.X[j, :].T

        # 第八步：根据b1，b2，更新b
        if (os.alphas[i] > 0) and (os.alphas[i] < os.C):
            os.b = b1
        elif (os.alphas[j] > 0) and (os.alphas[j] < os.C):
            os.b = b2
        else:
            os.b = (b1 + b2) / 2.0
        return 1
    else:
        return 0


def smoP(data_mat, class_labels, C, toler, max_iter, k_tup=('lin', 0)):
    os = OptStruct(np.mat(data_mat), np.mat(class_labels).transpose(), C, toler)
    iter_num = 0
    entire_set = True
    alpha_pairs_changed = 0
    while (iter_num < max_iter) and (alpha_pairs_changed > 0 or entire_set):
        alpha_pairs_changed = 0
        if entire_set:
            # 遍历所有的值
            for i in range(os.m):
                alpha_pairs_changed += innerL(i, os)
                print("fullSet, iter: %d i:%d, pairs changed %d" % (iter_num, i, alpha_pairs_changed))
            iter_num += 1
        else:
            # 遍历非边界值
            # alphas中选择出alpha大于0小于C的数据
            non_bound_is = np.nonzero((os.alphas.A > 0) * (os.alphas.A < C))[0]
            for i in non_bound_is:
                alpha_pairs_changed += innerL(i, os)
                print("non-bound, iter: %d i:%d, pairs changed %d" % (iter_num, i, alpha_pairs_changed))
            iter_num += 1
        if entire_set:
            entire_set = False
        elif alpha_pairs_changed == 0:
            entire_set = True
        print("iteration number: %d" % iter_num)
    return os.b, os.alphas


def calc_ws(data_mat, label_mat, alphas):
    """
    计算w向量
    :param data_mat: 特征向量
    :param label_mat: 标签数据
    :param alphas: 由smo算法计算出来的alphas
    :return: 返回w向量 也就是超平面的法向量
    """
    data_mat, label_mat = np.mat(data_mat), np.mat(label_mat).transpose()
    m, n = np.shape(data_mat)
    w = np.zeros((n, 1))
    for i in range(m):
        w += np.multiply(alphas[i] * label_mat[i], data_mat[i, :].T)
    return w

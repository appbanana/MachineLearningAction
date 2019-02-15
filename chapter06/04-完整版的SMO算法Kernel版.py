import time
# 完整版的SMO算法核函数版
import svmFullKernel
import numpy as np
from matplotlib import pyplot as plt

# 指定默认字体 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


def test_rbf(k1=1.3):
    # 加载训练集
    data_arr, label_arr = svmFullKernel.load_dataset('./data/testSetRBF.txt')
    # 简化版smo算法 获得一系列的alphas和b
    b, alphas = svmFullKernel.smoP(data_arr, label_arr, 200, 0.0001, 10000, ('rbf', k1))
    data_mat = np.mat(data_arr)
    label_mat = np.mat(label_arr).transpose()
    # np.nonzero(alphas.A > 0) 筛选出alphas中大于0的数据的索引 返回两个数组
    # print(np.nonzero(alphas.A > 0))
    # (array([ 0,  1,  3, 10, 13, 14, 16, 17, 18, 19, 21, 26, 27, 28, 29, 31, 36,41, 42, 45, 50, 54, 56, 62, 76, 87]),
    # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    sv_ind = np.nonzero(alphas.A > 0)[0]
    # 取出alpha不为0对应的特征向量
    svs = data_mat[sv_ind]
    print(f"支持向量个数:{svs.shape[0]}")

    # 取出alpha不为0对应的标签向量
    label_sv = label_mat[sv_ind]
    m, n = np.shape(data_mat)
    error_count = 0
    for i in range(m):
        # kernel_trans(X, A, k_tup):
        kernel_eval = svmFullKernel.kernel_trans(svs, data_mat[i, :], ('rbf', k1))
        predict = kernel_eval.T * np.multiply(label_sv, alphas[sv_ind]) + b
        if np.sign(predict) != np.sign(label_arr[i]):
            error_count += 1
    acc_train = 1 - float(error_count) / m
    print("训练集上的准确率: %f" % acc_train)

    # 在测试集上验证svm
    # 加载测试集
    data_arr, label_arr = svmFullKernel.load_dataset('./data/testSetRBF2.txt')
    data_mat, label_mat = np.mat(data_arr), np.mat(label_arr).transpose()
    m, n = np.shape(data_mat)
    error_count = 0

    for i in range(m):
        kernel_eval = svmFullKernel.kernel_trans(svs, data_mat[i, :], ('rbf', k1))
        predict = kernel_eval.T * np.multiply(label_sv, alphas[sv_ind]) + b
        if np.sign(predict) != np.sign(label_arr[i]):
            error_count += 1
    acc_test = 1 - float(error_count) / m
    print("测试集上的准确率: %f" % acc_test)
    return acc_train, acc_test


def show_acc_plot():
    train_acc = []
    test_acc = []
    for i in range(10):
        a, b = test_rbf(1.3)
        train_acc.append(a)
        test_acc.append(b)
    plt.plot(range(1, 11), train_acc, label='train_acc')
    plt.plot(range(1, 11), test_acc, label='test_acc')
    plt.xlabel('次数')
    plt.ylabel('模型准确率')
    plt.legend()
    plt.savefig('{0}.png'.format('./img/Figure_04_1'))
    plt.show()


def show_k1_plot():
    """
    由Figure_04_2图可知 rbf随k1的变大准确率先直接下降在提升 在平稳
    可以联想到局部优化提升预测率
    :return:
    """
    train_acc = []
    test_acc = []
    # k1_arr = list(range(1, 100, 10))
    # 局部优化提升预测率
    k1_arr = list(range(0.1, 3, 10))
    for i in range(len(k1_arr)):
        a, b = test_rbf(k1_arr[i])
        train_acc.append(a)
        test_acc.append(b)
    plt.figure()
    plt.plot(k1_arr, train_acc, label='train_acc')
    plt.xlabel('k1')
    plt.ylabel('模型准确率')
    plt.legend()
    plt.savefig('{0}.png'.format('./img/Figure_04_2'))
    plt.show()


if __name__ == '__main__':
    # 训练和测试算法
    _, _ = test_rbf()

    # 绘制训练集和测试集的准确率
    show_acc_plot()
    show_k1_plot()

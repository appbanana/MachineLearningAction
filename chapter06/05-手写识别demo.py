import os
import numpy as np
# 完整版的SMO算法核函数版
import svmFullKernel
import pandas as pd


def img_2_vector(filename):
    """
    将32 x 32的二进制图像转化为1 x 1024的向量
    :param filename:
    :return:
    """
    return_vect = np.zeros((1, 1024))
    with open(filename, 'r') as fr:
        for i in range(32):
            line_str = fr.readline()
            for j in range(32):
                return_vect[0, 32 * i + j] = int(line_str[j])
        return return_vect


def load_images_digits(file_path):
    """
    加载图片
    :param file_path: 文件路径
    :return: 返回特征矩阵和标签矩阵
    """
    training_file_list = os.listdir(file_path)
    m = len(training_file_list)
    # 存储训练样本数据
    data_mat = np.zeros((m, 1024))
    # 存储训练样本的标签
    hw_labels = []
    for i in range(m):
        file_name = training_file_list[i]
        label = file_name.split('_')[0]
        if label == '9':
            hw_labels.append(-1)
        else:
            hw_labels.append(1)
        data_mat[i, :] = img_2_vector(file_path + file_name)
    return data_mat, hw_labels


def test_digits(k_tup=('rbf', 10)):
    """
    径向核函数预测手写数字
    :param k_tup:
    :return:
    """
    data_arr, label_arr = load_images_digits('./data/digits/trainingDigits/')
    b, alphas = svmFullKernel.smoP(data_arr, label_arr, 200, 0.0001, 10000, k_tup)
    data_mat, label_mat = np.mat(data_arr), np.mat(label_arr).transpose()
    sv_ind = np.nonzero(alphas.A > 0)[0]
    # 筛选出支持向量
    svs = data_mat[sv_ind]
    label_sv = label_mat[sv_ind]
    print('有%d个支持向量' % np.shape(svs)[0])
    m, n = np.shape(data_mat)
    error_count = 0
    for i in range(m):
        kernel_eval = svmFullKernel.kernel_trans(svs, data_mat[i, :], k_tup)
        predict = kernel_eval.T * np.multiply(label_sv, alphas[sv_ind]) + b
        if np.sign(predict) != np.sign(label_arr[i]):
            error_count += 1
    train_acc = 1 - 1.0 * error_count / m
    print('训练集上准确率为：%f' % train_acc)

    # 测试集上验证
    data_arr, label_arr = load_images_digits('./data/digits/testDigits/')
    data_mat, label_mat = np.mat(data_arr), np.mat(label_arr).transpose()
    m, n = np.shape(data_mat)

    error_count = 0
    for i in range(m):
        kernel_eval = svmFullKernel.kernel_trans(svs, data_mat[i, :], k_tup)
        predict = kernel_eval.T * np.multiply(label_sv, alphas[sv_ind]) + b
        if np.sign(predict) != np.sign(label_arr[i]):
            error_count += 1
    test_acc = 1 - 1.0 * error_count / m
    print('训练集上准确率为：%f' % test_acc)
    return train_acc, test_acc, svs.shape[0]


if __name__ == '__main__':
    _, _, _ = test_digits()

    # 测试delta
    acc_train = []
    acc_test = []
    svm_num = []
    k_tups = [('rbf', 0.1), ('rbf', 5), ('rbf', 10), ('rbf', 50), ('rbf', 100), ('lin', 0)]
    for k_tup in k_tups:
        a, b, c = test_digits(k_tup)
        acc_train.append(a)
        acc_test.append(b)
        svm_num.append(c)
    df = pd.DataFrame({'内核设置': k_tups,
                       '训练准确率': acc_train,
                       '测试准确率': acc_test,
                       '支持向量数': svm_num,
                       })
    for i in df.columns[1:-1]:
        df.loc[:, i] = [round(x * 100, 1) for x in df.loc[:, i].values]
    print(df)
    """
         内核设置  训练准确率  测试准确率  支持向量数
    0  (rbf, 0.1)  100.0   47.8    402
    1    (rbf, 5)  100.0   96.8    402
    2   (rbf, 10)  100.0  100.0    128
    3   (rbf, 50)   99.3   98.9     51
    4  (rbf, 100)  100.0   98.9     43
    5    (lin, 0)  100.0   98.4     49

    """

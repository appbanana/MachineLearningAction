import adaboost
import numpy as np
from matplotlib import pyplot as plt

# 指定默认字体 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


def show_plot(dat_mat, label_arr):
    print('******' * 15)
    data_array = np.array(dat_mat)
    label_array = np.array(label_arr)
    plt.scatter(data_array[:, 0], data_array[:, 1], c=label_array)
    plt.savefig('{0}.png'.format('./img/Figure_01'))
    plt.show()


def stump_classify(dat_mat, dim, thresh_val, thresh_ineq):
    """
    将数据按照阈值进行分类 阈值一侧为+1类 另一侧为-1类
    :param dat_mat: 特征数据
    :param dim: 都一个特征维度
    :param thresh_val: 阈值
    :param thresh_ineq: 阈值的左边或者右边
    :return: 返回预测的分类
    """
    ret_array = np.ones((np.shape(dat_mat)[0], 1))
    if thresh_ineq == 'lt':
        ret_array[dat_mat[:, dim] <= thresh_val] = -1.0
    else:
        ret_array[dat_mat[:, dim] > thresh_val] = -1.0
    return ret_array


def build_stump(data_mat, class_labels, D):
    """
    寻找最佳的单层决策树
    :param data_mat: 特征数据
    :param class_labels: 标签数据
    :param D: 权重向量D
    :return: 错误率最小的单层决策树，最小错误率，预测结果
    """
    data_mat, label_mat = np.mat(data_mat), np.mat(class_labels).T
    m, n = np.shape(data_mat)
    num_steps = 10.0
    best_stump = {}
    best_class_est = np.mat(np.zeros((m, 1)))
    min_error = np.inf
    for i in range(n):
        range_min = data_mat[:, i].min()
        range_max = data_mat[:, i].max()
        step_size = (range_max - range_min) / num_steps
        for j in range(-1, int(num_steps) + 1):
            for inequal in ['lt', 'gt']:
                thresh_val = range_min + float(j) * step_size
                predicted_vals = stump_classify(data_mat, i, thresh_val, inequal)
                error_arr = np.mat(np.ones((m, 1)))
                # 将预测正确的置位0 便于同于错误率
                error_arr[predicted_vals == label_mat] = 0
                weight_error = D.T * error_arr
                # print('######' * 10)
                # print(predicted_vals)
                # print("split: dim %d, thresh %.2f, thresh inequal: %s, the weighted error is %.3f" % (i, thresh_val, inequal, weight_error))
                if weight_error < min_error:
                    min_error = weight_error
                    best_class_est = predicted_vals.copy()
                    best_stump['dim'] = i
                    best_stump['thresh'] = thresh_val
                    best_stump['ineq'] = inequal
    return best_stump, min_error, best_class_est


def adaboost_train_ds(data_mat, class_labels, max_iter=40):
    """
    adaBoost训练最佳单层决策树
    :param data_mat: 特征矩阵
    :param class_labels: 标签矩阵
    :param max_iter: 最大循环次数
    :return:
    """
    weak_class_arr = []
    m = np.shape(data_mat)[0]
    D = np.mat(np.ones((m, 1)) / m)
    agg_class_est = np.mat(np.zeros((m, 1)))
    for i in range(max_iter):
        best_stump, min_error, predict_value, = build_stump(dat_arr, labels_arr, D)
        print('D:', D.T)
        # 计算alpha值
        alpha = float(0.5 * np.log((1.0 - min_error) / max(min_error, 1e-16)))
        best_stump['alpha'] = alpha
        weak_class_arr.append(best_stump)
        print("predict_value: ", predict_value.T)

        # Di(t+1) = Di(t) * exp(-α*yi*ht(xi)) / sum(D)  其实ht(xi) 就是预测predict_value
        # 预测对的减少权重 预测错的增大权重
        expon = np.multiply(-1 * alpha * np.mat(class_labels).T, predict_value)
        D = np.multiply(D, np.exp(expon))
        D = D / np.sum(D)
        agg_class_est += alpha * predict_value
        print("agg_class_est: ", agg_class_est.T)
        # np.sign(agg_class_est) != np.mat(class_labels).T 将错误的置位1 对的置位0 便于统计错误的个数
        agg_errors = np.multiply(np.sign(agg_class_est) != np.mat(class_labels).T, np.ones((m, 1)))
        error_rate = agg_errors.sum() / m
        print('total error:', error_rate)
        if error_rate == 0:
            break
    return weak_class_arr


def ada_classify(data_mat, classifier_arr):
    """
    ada分类函数
    :param data_mat: 特征矩阵
    :param classifier_arr: 弱分类器数组
    :return: 返回预测的分类
    """
    data_mat = np.mat(data_mat)
    m = np.shape(data_mat)[0]
    agg_class_est = np.mat(np.zeros((m, 1)))
    for index, item in enumerate(classifier_arr):
        class_predict = stump_classify(data_mat, item['dim'], item['thresh'], item['ineq'])
        agg_class_est += item['alpha'] * class_predict
        print(agg_class_est)
    return np.sign(agg_class_est)


if __name__ == '__main__':
    # 加载简单的数据
    dat_arr, labels_arr = adaboost.load_simple_data()

    # show_plot(dat_arr, labels_arr)
    # m = np.shape(dat_arr)[0]
    # D = np.mat(np.ones((m, 1)) / m)

    # 最佳单层决策树
    # best_stump, error, predict_value, = build_stump(dat_arr, labels_arr, D)
    # print(best_stump, error)
    # print(predict_value)

    weak_class_arr = adaboost_train_ds(dat_arr, labels_arr, 30)
    print('********' * 10)
    print(weak_class_arr)

    print('*****分类*****' * 10)
    predicted = ada_classify([0, 0], weak_class_arr)
    print(predicted)
    print('*****' * 10)
    predicted = ada_classify([[0, 0], [5, 5]], weak_class_arr)
    print(predicted)

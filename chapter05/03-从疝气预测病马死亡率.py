import logRegres
import numpy as np


def load_data(filename):
    """
    加载数据
    :param filename: 文件路径
    :return:
    """
    features_mat = []
    class_labels = []
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        print(len(lines))
        for line in lines:
            current_line = line.strip().split('\t')
            features_mat.append(current_line[:-1])
            class_labels.append(current_line[-1])
        return np.array(features_mat).astype(float), np.array(class_labels).astype(float)


if __name__ == '__main__':

    # 加载数据 horseColicTest.txt 总共67条数据 22个属性
    file_name = './data/horseColicTest.txt'
    X_train, y_train = load_data(file_name)

    # 训练数据 用来预测测试数据 计算回归系数
    train_weights = logRegres.stoc_grad_ascent1(X_train, y_train, max_iter=500)

    # 加载测试数据 用来验证数据预测的准确性
    file_name = './data/horseColicTraining.txt'
    # 加载测试数据
    X_test, y_test = load_data(file_name)
    # 用来统计预测正确的样本数
    count = 0
    # 遍历测试数据集
    for i in range(len(X_test)):
        test_data = X_test[i]
        # 预测测试数据
        pred_label = logRegres.classify_vector(test_data, train_weights)
        # 预测的标签和真实的比较
        if int(pred_label) == y_test[i]:
            count += 1
    # 计算正确率
    right_percent = 1.0 * count / len(y_test)
    print(right_percent)

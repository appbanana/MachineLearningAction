import numpy as np
import operator
from collections import defaultdict


def create_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(test_data, train_data, labels, k):
    """
    :param test_data: 待测数据
    :param train_data: 训练集数据
    :param labels: 标签
    :param k: k值
    :return: 返回所属分类
    """
    sample_size = len(train_data)
    test_data = np.tile(test_data, (sample_size, 1))
    # 计算待测点距离训练集的欧氏距离
    delta = (test_data - train_data) ** 2
    distance = np.sqrt(np.sum(delta, axis=1))

    # # 对距离按近到远排序
    sort_distance = np.argsort(distance)
    count_dic = defaultdict(int)
    # 统计最近的K个数据
    for i in range(k):
        vote_label = labels[sort_distance[i]]
        # count_dic[vote_label] += 1
        count_dic[vote_label] = count_dic.get(vote_label, 0) + 1
    # 对投票进行排序
    sort_count_dic = sorted(count_dic.items(), key=operator.itemgetter(1), reverse=True)
    return sort_count_dic[0][0]


def auto_norm(data_set):
    """
    数据最大值最小值规范化
    :param data_set: 输入的数据集
    :return: 规范后的数据，区间， 最小值，最大值
    """
    min_val = data_set.min(0)
    max_val = data_set.max(0)
    ranges = max_val - min_val

    return (data_set - min_val) / ranges, min_val, ranges


def load_dataset(file_name):
    """
    不使用其他库加载文件加载数据
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        number_lines = f.readlines()
        feature_mat = np.zeros((len(number_lines), 3))
        class_label = []
        index = 0
        for line in number_lines:
            line = line.strip()
            list_content = line.split('\t')
            feature_mat[index, :] = list_content[0:3]
            class_label.append(list_content[-1])
            index += 1
        return feature_mat, class_label


def test_KNN(data, labels, ratio=0.5):
    """
    测试KNN算法的准确率
    :param data: 数据
    :param labels: 标签
    :param ratio: 用于测试的比例
    :return:
    """
    test_number = int(ratio * len(data))
    score_count = 0
    for i in range(test_number):
        result = classify(data[i, :], data[test_number:, :], labels=labels[test_number:], k=3)
        if result == labels[i]:
            score_count += 1.0

    return 1.0 * score_count / test_number

import collections
import numpy as np


def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


def calc_shannon_ent(dataset):
    """
    计算信息熵
    :param dataSet: 输入的数据集
    :return:
    """
    total_number = len(dataset)
    count_dic = collections.defaultdict(int)
    for i in range(total_number):
        label = dataset[i][-1]
        count_dic[label] += 1
    cal_result = 0
    for key, value in count_dic.items():
        temp_p = 1.0 * value / total_number
        cal_result += (-temp_p * np.log2(temp_p))
    return cal_result


def split_dataset(dataset, axis, value):
    ret_dataset = []
    for feat_vec in dataset:
        if feat_vec[axis] == value:
            # 去掉axis=value的特征值
            reduce_feat_vec = feat_vec[:axis]
            reduce_feat_vec.extend(feat_vec[axis + 1:])
            ret_dataset.append(reduce_feat_vec)
    return ret_dataset


def choose_best_feature_to_split(dataset):
    """
    计算每个特征的信息增益 并返回信息增益最大的特征
    :param dataset:
    :return:
    """
    feature_num = len(dataset[0]) - 1
    base_entropy = calc_shannon_ent(dataset)
    base_info_gain = 0.0
    best_feature = -1
    for i in range(feature_num):
        # 取出各个特征值
        feature_list = [example[i] for example in dataset]
        # 特征值去重 看一下特征值一共有多少取值
        unique = set(feature_list)
        new_entropy = 0.0  # 经验条件熵
        for feature_value in unique:
            # 取出特征值等于feature_value的所有数据
            sub_dataset = split_dataset(dataset, i, feature_value)
            print(sub_dataset)
            # 计算子集的的概率
            # 这个参考《Python 数据分析与挖掘实战》P104页 你就明白了
            prob = len(sub_dataset) / len(dataset)
            new_entropy += prob * calc_shannon_ent(sub_dataset)
        # 计算某个特征值的信息增益
        info_gain = base_entropy - new_entropy
        if info_gain > base_info_gain:
            base_info_gain = info_gain
            best_feature = i
    return best_feature


if __name__ == '__main__':
    my_data, class_labels = create_dataset()
    result = calc_shannon_ent(my_data)
    # 0.9709505944546686
    print(result)

    print('******' * 10)
    my_data[0][-1] = 'maybe'
    result = calc_shannon_ent(my_data)
    # 1.3709505944546687
    print(result)

    print('******' * 10)
    my_data, class_labels = create_dataset()
    result = split_dataset(my_data, 0, 1)
    print(result)
    result = split_dataset(my_data, 0, 0)
    print(result)

    print('***###***' * 10)
    # 寻找最好的特性来分割数据
    choose_best_feature_to_split(my_data)

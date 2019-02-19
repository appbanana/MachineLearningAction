import collections
import operator
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
        # 筛选出特征值值等于 value的值
        if feat_vec[axis] == value:
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


def majority_cnt(class_list):
    """
    返回类别中出现频率最高的标签
    :param class_list:
    :return:
    """
    class_count = collections.defaultdict(int)
    for vote in class_list:
        class_count[vote] += 1
    sort_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sort_class_count[0][0]


def create_tree(dataset, labels):
    """
    创建树形结构
    :param dataset: 输入的数据集
    :param labels: 标签
    :return: 返回树
    """

    # print('****' * 20)
    # print(dataset)
    # print(labels)

    # 取出分类标签
    class_list = [example[-1] for example in dataset]
    # 如果类别相同 就停止划分
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 遍历完所有的特征时 返回出现次数最多的标签
    if len(dataset[0]) == 1 or len(labels) == 0:
        return majority_cnt(labels)
    # 筛选出最好的特征值
    best_feature = choose_best_feature_to_split(dataset)
    best_feat_label = labels[best_feature]
    my_tree = {best_feat_label: {}}
    # print('+++++best_feature++++++')
    # print(best_feature)

    del (labels[best_feature])
    best_feature_values = [example[best_feature] for example in dataset]
    unique_values = set(best_feature_values)

    for value in unique_values:
        sub_labels = labels[:]
        split_data = split_dataset(dataset, best_feature, value)
        # print('+++++split_Data++++++')
        # print(split_data)
        temp_value = create_tree(split_data, sub_labels)
        print(temp_value)
        my_tree[best_feat_label][value] = temp_value

    # print('my_tree----my_tree')
    # print(my_tree)
    return my_tree


def get_number_leafs(my_tree):
    """
    计算叶子节点的个数
    :param my_tree:
    :return:
    """
    # print('***********' * 10)
    # print(my_tree)
    num_leafs = 0
    first_str = list(my_tree.keys())[0]
    # print(first_str)
    second_dic = my_tree[first_str]
    # print(type(second_dic) == dict)
    # print(second_dic)
    # print(list(second_dic.keys()))
    for key in list(second_dic.keys()):
        if isinstance(second_dic[key], dict):
            # 如果是字典的话 这是判断节点
            num_leafs += get_number_leafs(second_dic[key])
        else:
            num_leafs += 1
    # print(num_leafs)
    return num_leafs


def get_tree_depth(my_tree):
    """
    计算树的深度
    :param my_tree:
    :return:
    """
    max_depth = 0
    fist_str = list(my_tree.keys())[0]
    second_dic = my_tree[fist_str]
    for key in list(second_dic.keys()):
        if isinstance(second_dic[key], dict):
            this_depth = 1 + get_tree_depth(second_dic[key])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth
    return max_depth


def classify(input_tree, feat_labels, test_vec):
    # 获取树的第一特征的名称 eg：'no surfacing'
    first_str = list(input_tree.keys())[0]
    sec_dict = input_tree[first_str]
    # 获取特征在feat_labels的所处的位置
    feat_index = feat_labels.index(first_str)
    # 获取测试属性 对应的特征值 eg：0 or 1
    key = test_vec[feat_index]
    # 获取特征值在树中对应的value
    feat_value = sec_dict[key]
    if isinstance(feat_value, dict):
        class_label = classify(feat_value, feat_labels, test_vec)
    else:
        class_label = feat_value
    return class_label


def store_tree(input_tree, file_name):
    """
    序列化数据
    :param input_tree: 树结构（字典类型的）
    :param file_name: 文件路径
    :return:
    """
    import pickle
    import json
    with open(file_name, 'wb') as fw:
        # json.dumps(d)
        pickle.dump(input_tree, fw)


def grab_tree(file_name):
    """
    反序列化数据
    :param file_name: 文件路径
    :return:
    """
    import pickle
    f = open(file_name, 'rb')
    data = pickle.load(f)
    f.close()
    return data

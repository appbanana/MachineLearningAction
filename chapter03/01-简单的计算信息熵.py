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


if __name__ == '__main__':
    my_data, class_labels = create_dataset()
    result = calc_shannon_ent(my_data)
    # 0.9709505944546686
    print(result)

    my_data[0][-1] = 'maybe'
    result = calc_shannon_ent(my_data)
    # 1.3709505944546687
    print(result)


import pandas as pd
import numpy as np
import KNN
from matplotlib import pyplot as plt

# 指定默认字体 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


def load_dataset(file_name):
    """
    使用pandas加载文件
    :param file_name: 文件路径
    :return: 加载好的数据
    """
    data_set = pd.read_csv(file_name, header=None, sep='\t')
    data_set.loc[data_set.iloc[:, -1] == 'largeDoses', 3] = 1
    data_set.loc[data_set.iloc[:, -1] == 'smallDoses', 3] = 2
    data_set.loc[data_set.iloc[:, -1] == 'didntLike', 3] = 3
    data_set.columns = [u'每年获得的飞行常客里程数', u'玩游戏所消耗时间百分比', u'每周消费的冰激凌公升数', u'样本分类']
    return data_set


def plot_data(data):
    plt.figure()
    colors = ['red', 'green', 'blue']
    labels = [u'极具魅力', u'魅力一般', u'不喜欢']
    for i in range(1, 4):
        temp_data = data[data.iloc[:, -1] == i]
        plt.scatter(temp_data.iloc[:, 0], temp_data.iloc[:, 1], s=(4 - i) * 15, c=colors[i - 1], label=labels[i - 1])
    plt.legend()
    plt.xlabel(u'每年获得的飞行常客里程数')
    plt.ylabel(u'玩游戏所消耗时间百分比')
    plt.savefig('{0}.png'.format('./img/Figure_01'))
    plt.show()


def classify_people():
    """
    预测输入的数据
    :return: 返回结果标签
    """
    result = ['didntLike', 'smallDoses', 'largeDoses']
    percent_game = float(input('玩游戏所消耗时间百分比 :\t'))
    fly_miles = float(input('每年获得的飞行常客里程数:\t'))
    ice_cream = float(input('每周消费的冰激凌公升数:\t'))

    features, label = KNN.load_dataset('./data/datingTestSet2.txt')
    _, min_value, ranges_value = KNN.auto_norm(features_mat)
    data_array = np.array([fly_miles, percent_game, ice_cream])
    data_array = (data_array - min_value) / ranges_value
    result_index = KNN.classify(data_array, norm_data, labels=label, k=3)
    result_index = int(result_index)
    print(result[result_index - 1])


if __name__ == '__main__':
    # 不使用其他库加载处理数据
    features_mat, class_label = KNN.load_dataset('./data/datingTestSet2.txt')
    # 数据归一化
    norm_data, min_val, ranges = KNN.auto_norm(features_mat)
    # 训练数据
    score = KNN.test_KNN(norm_data, labels=class_label, ratio=0.5)
    print(score)  # 0.934
    # 预测数据
    classify_people()

    # 使用pandas 加载数据
    # data = load_dataset('./data/datingTestSet.txt')
    # 绘制图形
    # plot_data(data)


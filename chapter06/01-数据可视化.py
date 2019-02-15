import svm
import numpy as np
from matplotlib import pyplot as plt


def show_dataset(x_data, y_labels):
    """
    数据可视化
    :param x_data: 输入的数据
    :param y_labels: 标签数据
    """
    data_p = []
    data_n = []
    # 数据长度
    data_len = len(x_data)
    for i in range(data_len):
        if y_labels[i] > 0:
            data_p.append(x_data[i])
        else:
            data_n.append(x_data[i])
    data_p = np.array(data_p)
    data_n = np.array(data_n)
    # 散点图
    plt.scatter(np.transpose(data_p)[0], np.transpose(data_p)[1])
    plt.scatter(np.transpose(data_n)[0], np.transpose(data_n)[1])
    plt.savefig('{0}.png'.format('./img/Figure_01'))
    plt.show()


if __name__ == '__main__':
    # svm参考文章 写的非常还 https://blog.csdn.net/c406495762/article/details/78072313
    data_arr, label_arr = svm.load_dataset('./data/testSet.txt')
    show_dataset(data_arr, label_arr)

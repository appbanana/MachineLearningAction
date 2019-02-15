import time
# 完整版的SMO算法
import svmFull
import numpy as np
from matplotlib import pyplot as plt


def show_classifer(x_data, y_labels, w, b):
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
    # 绘制散点图
    plt.scatter(np.transpose(data_p)[0], np.transpose(data_p)[1], s=30, alpha=0.7)
    plt.scatter(np.transpose(data_n)[0], np.transpose(data_n)[1], s=30, alpha=0.7)
    # 绘制超平面 此时超平面是一条直线
    x1 = max(x_data)[0]
    x2 = min(x_data)[0]
    # w是一个二维数组
    a1, a2 = w
    b = float(b)
    a1 = float(a1[0])
    a2 = float(a2[0])
    y1, y2 = (-b - a1 * x1) / a2, (-b - a1 * x2) / a2
    plt.plot([x1, x2], [y1, y2])
    # 找出支持向量点
    for i, alpha in enumerate(alphas):
        if abs(alpha) > 0:
            x, y = data_arr[i]
            plt.scatter([x], [y], s=150, edgecolors='red', alpha=0.7, linewidth=1.5)
    plt.savefig('{0}.png'.format('./img/Figure_03'))
    plt.show()


if __name__ == '__main__':
    # svm参考文章 写的非常还 https://blog.csdn.net/c406495762/article/details/78072313
    data_arr, label_arr = svmFull.load_dataset('./data/testSet.txt')
    start = time.process_time()
    # 简化版smo算法 获得一系列的alphas和b
    b, alphas = svmFull.smoP(data_arr, label_arr, 0.6, 0.001, 40)
    end = time.process_time()
    # 完整版花费时间为：0.075445
    print('完整版花费时间为：%f' % (end - start))
    print(alphas)
    # 计算w向量 w向量出来就意味着超平面的确定
    w = svmFull.calc_ws(data_arr, label_arr, alphas)
    print(w)
    show_classifer(data_arr, label_arr, w, b)

    # 测试分类 结果小于0 则为-1分类 大于0则为1分类
    data_mat = np.mat(data_arr)
    # 测试第一个数据
    print('测试第一个数据')
    print(data_mat[0] * np.mat(w) + b)
    # 测试第二个数据
    print('测试第二个数据')
    print(data_mat[2] * np.mat(w) + b)


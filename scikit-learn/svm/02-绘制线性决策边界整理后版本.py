from sklearn import datasets
from sklearn import svm
import numpy as np
from matplotlib import pyplot as plt


def plot_svc_decision_function(model, ax=None):
    if ax is None:
        ax = plt.gca()
    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()
    axis_x = np.linspace(x_lim[0], x_lim[1], num=30)
    axis_y = np.linspace(y_lim[0], y_lim[1], num=30)
    # 将上面的点形成30 * 30 个网格点 将两个一维向量转换为特征矩阵
    axis_x, axis_y = np.meshgrid(axis_x, axis_y)
    # ravel 拉平降维 在转置把数据变成900个点
    xy = np.vstack([axis_x.ravel(), axis_y.ravel()]).T
    # 绘画网格图上点 900个
    plt.scatter(xy[:, 0], xy[:, 1], s=1, cmap='rainbow')
    """
    np.vstack([[1, 2, 3], [4, 5, 6]]).T
    array([[1, 4],
           [2, 5],
           [3, 6]])
    """
    # 返回每个输入样本到决策边界的距离 然后在将这个距离转换为axis_x结构，这是由于画图的函数要求Z的结构必须与X和Y保持一致
    Z = model.decision_function(xy).reshape(axis_x.shape)
    # levels= [-1, 0, 1] 三条等高线 代表点到决策边界的集合距离 axis_x 30 * 30
    ax.contour(axis_x, axis_y, Z, color='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
    plt.xticks(x_lim)
    # 设置x轴坐标显示，标签的展示，标签的旋转角度
    # plt.xticks(ticks=np.arange(-9, -1), labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], rotation=-30)
    plt.yticks(y_lim)


if __name__ == '__main__':
    # 生成簇行数据
    X, y = datasets.make_blobs(n_samples=100, centers=2, random_state=66, cluster_std=0.6)
    # (100, 2)
    print(np.shape(X))
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')

    clf = svm.SVC(kernel='linear').fit(X, y)
    plot_svc_decision_function(clf)

    plt.show()

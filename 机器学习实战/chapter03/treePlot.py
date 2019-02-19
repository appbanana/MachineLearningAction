import matplotlib.pyplot as plt
import tree

# 指定默认字体 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


def plot_node(s, xy, xytext, bbox, arrowprops=dict(facecolor='black', arrowstyle='<-')):
    plot.ax.annotate(s, xy=xy, xytext=xytext,
                     arrowprops=arrowprops,
                     bbox=bbox
                     )


# def create_plot():
#     fig, ax = plt.subplots()
#     plot_node(ax, s='决策树节点', xy=(0.2, 0.8), xytext=(0.5, 0.1), bbox=dict(boxstyle='round', fc="w", ec="k"))
#     plot_node(ax, s='叶子点', xy=(0.2, 0.8), xytext=(0.5, 0.3), bbox=dict(boxstyle='sawtooth', fc="w", ec="k"))
#     ax.set_ylim(0, 1)
#     ax.set_xlim(0, 1)
#     plt.show()


def plot_tree():
    # first_str = list(my_tree.keys())[0]
    # second_dic = my_tree[first_str]
    # plot_node(ax, s=first_str, xy=(0.2, 0.8), xytext=(0.5, 0.1), bbox=dict(boxstyle='round', fc="w", ec="k"))
    # for key in list(second_dic.keys()):
    #     if isinstance(second_dic[key], dict):
    #         # 如果是字典的话 这是判断节点
    #         plot_tree(second_dic[key], ax, key)
    #
    #     else:
    #         plot_node(ax, s=key, xy=(0.2, 0.8), xytext=(0.5, 0.3), bbox=dict(boxstyle='sawtooth', fc="w", ec="k"))
    #         # num_leafs += 1

    ax.annotate(s='决策树节点', xy=(0.2, 0.8), xytext=(0.5, 0.1), bbox=dict(boxstyle='round', fc="w", ec="k"))
    plt.show()


def create_plot(my_tree):
    # plt.figure(num=6)
    fig, ax = plt.subplots(nrows=1, ncols=1)

    num_leafs = tree.get_number_leafs(my_tree)
    tree_depth = tree.get_tree_depth(my_tree)
    ax.set_ylim(0, tree_depth)
    ax.set_xlim(0, num_leafs)

    print('*******' * 15)
    print(num_leafs, tree_depth)
    print(my_tree)

    while True:
        for item, value in my_tree.items():
            print('##########')
            print(item)
            print(value)
            print(type(item))
            if isinstance(value, dict):
                # 如果是字典的话 这是判断节点
                # fist_str = list(my_tree.keys())[0]
                # second_dic = my_tree[fist_str]
                if not isinstance(item, int):

                    ax.annotate(s=item, xy=(0.2, 0.8), xytext=(num_leafs * 0.5, tree_depth),
                                arrowprops=dict(facecolor='black', arrowstyle='<-'),
                                bbox=dict(boxstyle='round', fc="w", ec="k"))
                    my_tree = value
                    tree_depth -= 1
                else:
                    my_tree = value

            else:
                # 叶子节点
                ax.annotate(s=value, xy=(0.2, 0.8), xytext=(num_leafs * 0.5, tree_depth),
                            arrowprops=dict(facecolor='black', arrowstyle='<-'),
                            bbox=dict(boxstyle='sawtooth', fc="w", ec="k"))
        if tree_depth < 0:
            break
    plt.show()


def retrieve_tree(i):
    """
    测试树集
    :param i: 下标
    :return: 返回对应的树
    """
    list_trees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}},
                  ]
    return list_trees[i]

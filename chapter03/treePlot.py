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


def plot_tree(my_tree, node_text):
    first_str = list(my_tree.keys())[0]
    second_dic = my_tree[first_str]
    plot_node(ax, s=first_str, xy=(0.2, 0.8), xytext=(0.5, 0.1), bbox=dict(boxstyle='round', fc="w", ec="k"))
    for key in list(second_dic.keys()):
        if isinstance(second_dic[key], dict):
            # 如果是字典的话 这是判断节点
            plot_tree(second_dic[key], ax, key)

        else:
            plot_node(ax, s=key, xy=(0.2, 0.8), xytext=(0.5, 0.3), bbox=dict(boxstyle='sawtooth', fc="w", ec="k"))
            # num_leafs += 1


def create_plot(my_tree):
    plt.figure()
    plot.ax = plt.subplots()
    plot_tree(my_tree,  node_text='')

    num_leafs = tree.get_number_leafs(my_tree)
    tree_depth = tree.get_tree_depth(my_tree)
    ax.set_ylim(0, tree_depth)
    ax.set_xlim(0, num_leafs)
    plt.show()

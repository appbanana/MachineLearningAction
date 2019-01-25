import treePlot
import tree

if __name__ == '__main__':
    # 构建树
    my_data, class_labels = tree.create_dataset()
    my_tree = tree.create_tree(my_data, class_labels)

    # number_leafs = tree.get_number_leafs(my_tree)
    # print(number_leafs)
    #
    # tree_depth = tree.get_tree_depth(my_tree)
    # print(tree_depth)
    treePlot.create_plot()
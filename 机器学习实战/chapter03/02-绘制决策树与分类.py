import treePlot
import tree

if __name__ == '__main__':
    # 构建树
    my_data, class_labels = tree.create_dataset()
    # my_tree = tree.create_tree(my_data, class_labels)

    # number_leafs = tree.get_number_leafs(my_tree)
    # print(number_leafs)
    #
    # tree_depth = tree.get_tree_depth(my_tree)
    # print(tree_depth)
    # treePlot.create_plot(my_tree)

    my_tree = treePlot.retrieve_tree(0)

    class_label = tree.classify(my_tree, class_labels, [1, 0])
    print(class_label)
import tree

if __name__ == '__main__':
    my_data, class_labels = tree.create_dataset()
    result = tree.calc_shannon_ent(my_data)
    # 0.9709505944546686
    print(result)

    print('******' * 10)
    my_data[0][-1] = 'maybe'
    result = tree.calc_shannon_ent(my_data)
    # 1.3709505944546687
    print(result)

    print('******' * 10)
    my_data, class_labels = tree.create_dataset()
    result = tree.split_dataset(my_data, 0, 1)
    print(result)
    result = tree.split_dataset(my_data, 0, 0)
    print(result)

    print('***###***' * 10)
    # 寻找最好的特性来分割数据
    best_feature = tree.choose_best_feature_to_split(my_data)
    print(best_feature)

    print('########' * 10)
    # 构建树
    my_data, class_labels = tree.create_dataset()
    my_tree = tree.create_tree(my_data, class_labels)
    print('+++++tree++++++')
    print(my_tree)

    # 统计叶子节点
    print('+++++get_number_leafs++++++')
    number_leafs = tree.get_number_leafs(my_tree)
    print(number_leafs)

    tree_depth = tree.get_tree_depth(my_tree)
    print(tree_depth)
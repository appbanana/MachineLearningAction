import treePlot
import tree

if __name__ == '__main__':
    # 构建树
    my_data, class_labels = tree.create_dataset()

    my_tree = treePlot.retrieve_tree(0)
    tree.store_tree(my_tree, './data/classifier_storage.txt')

    load_data = tree.grab_tree('./data/classifier_storage.txt')
    print(load_data)


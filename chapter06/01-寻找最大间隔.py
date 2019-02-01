import svm

if __name__ == '__main__':
    data_arr, label_arr = svm.load_dataset('./data/testSet.txt')
    print(label_arr)
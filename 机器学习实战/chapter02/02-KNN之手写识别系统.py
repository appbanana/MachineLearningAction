import os
import numpy as np
import KNN


def img_2_vector(filename):
    """
    将32 x 32的二进制图像转化为1 x 1024的向量
    :param filename:
    :return:
    """
    return_vect = np.zeros((1, 1024))
    with open(filename, 'r') as fr:
        for i in range(32):
            line_str = fr.readline()
            for j in range(32):
                return_vect[0, 32 * i + j] = int(line_str[j])
        return return_vect


def hand_writing_class_test():
    """
    构建训练样本数据
    :return:
    """
    # ['5_135.txt', '4_36.txt', '8_102.txt', '8_116.txt', ....]
    dir_path = './data/trainingDigits/'
    training_file_list = os.listdir(dir_path)
    m = len(training_file_list)
    # 存储训练样本数据
    training_mat = np.zeros((m, 1024))
    # 存储训练样本的标签
    hw_labels = []
    for i in range(m):
        file_name = training_file_list[i]
        label = file_name.split('_')[0]
        hw_labels.append(label)
        training_mat[i, :] = img_2_vector(dir_path + file_name)

    # 读取测试样本数据 进行测试
    test_dir_path = './data/testDigits/'
    test_file_list = os.listdir(test_dir_path)
    m = len(test_file_list)
    count = 0
    for i in range(m):
        file_name = test_file_list[i]
        label = file_name.split('_')[0]
        temp_vector = img_2_vector(test_dir_path + file_name)
        pre_result = KNN.classify(temp_vector, training_mat, hw_labels, k=3)
        print("the classifier came back with: %s, the real answer is: %s" % (pre_result, label))
        if pre_result == label:
            count += 1.0
    # 正确率:0.988372
    print('正确率:%f' % (count / m))


if __name__ == '__main__':
    # test_vector = img_2_vector('./data/testDigits/0_13.txt')
    # print(test_vector[0, 0:31])
    # print(test_vector[0, 32:63])
    hand_writing_class_test()

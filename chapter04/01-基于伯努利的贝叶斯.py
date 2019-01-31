import bayes
import numpy as np

if __name__ == '__main__':
    # 获取测试数据
    list_word, class_label = bayes.load_dataset()
    print(list_word)
    print(class_label)

    # 所有单词的集合
    word_set = bayes.create_vocab_list(list_word)
    print(word_set)

    # 将社区评论转化为特征向量
    word_vec = bayes.set_of_word_2_vec(word_set, list_word[0])
    print(word_vec)

    # 将所有的评论数据 转化为特征矩阵
    train_mat = []
    for post_in_doc in list_word:
        word_vec = bayes.set_of_word_2_vec(word_set, post_in_doc)
        train_mat.append(word_vec)

    # 训练数据
    p0v, p1v, pab = bayes.train_nb0(train_mat, class_label)
    print(p0v)
    # print(p1v)
    # print(pab)

    # 测试
    print('***********' * 10)
    class_label = bayes.testing_nb()
    print(class_label)

    # 垃圾邮件测试 运行100次求平均
    result = []
    for i in range(100):
        correct_rate = bayes.spam_test()
        result.append(correct_rate)
    # 0.9
    print(np.mean(correct_rate))


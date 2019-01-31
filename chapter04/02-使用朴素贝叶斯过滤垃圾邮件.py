import bayes
import numpy as np


def spam_test():
    """
    data/email/spam 路径下邮件的测试
    :return: 返回正确率
    """
    doc_list = []
    class_list = []
    full_text = []

    for i in range(1, 26):
        # 读取email路径下spam中邮件内容
        email_content = open('./data/email/spam/%d.txt' % i, encoding='gbk').read()
        # 将邮件内容转化为单词数组
        word_list = bayes.text_parse(email_content)
        # word_list 二维数组 里面的每一个数组中代表一封邮件的内容
        doc_list.append(word_list)
        # 一维数组 将邮件中所有单词保存到full_text中
        full_text.extend(word_list)
        class_list.append(1)

        email_content = open('./data/email/ham/%d.txt' % i, encoding='gbk').read()
        word_list = bayes.text_parse(email_content)
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)

    trainset = list(range(50))
    testset = []
    for i in range(10):
        # 随机在（0, len(trainset)）范围内一个浮点数 在取整
        rand_index = int(np.random.uniform(0, len(trainset)))
        # 将随机到的下标 添加到测试集中
        testset.append(trainset[rand_index])
        # 同时在训练集中删除
        del trainset[rand_index]

    # 将所有邮件中的单词转化为特征向量
    voca_list = bayes.create_vocab_list(doc_list)
    train_mat = []
    train_class = []

    for doc_index in trainset:
        train_mat.append(bayes.set_of_word_2_vec(voca_list, doc_list[doc_index]))
        train_class.append(class_list[doc_index])

    # 训练数据
    p0v, p1v, p_spam = bayes.train_nb1(train_mat, train_class)
    # 统计正确的个数
    count = 0
    # 开始在测试集中验证结果是否正确
    for doc_index in testset:
        word_vec = bayes.set_of_word_2_vec(voca_list, doc_list[doc_index])
        if bayes.classify_nb(np.array(word_vec), p0v, p1v, p_spam) == class_list[doc_index]:
            # 统计正确的个数
            count += 1
    # 计算正确率
    rate = 1.0 * count / len(testset)
    return rate


if __name__ == '__main__':

    # 垃圾邮件测试 运行100次求平均
    result = []
    for i in range(100):
        correct_rate = spam_test()
        result.append(correct_rate)
    # 0.9
    print(np.mean(correct_rate))

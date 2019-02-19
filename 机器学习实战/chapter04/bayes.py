import numpy as np


def load_dataset():
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return posting_list, class_vec


def create_vocab_list(dataset):
    """
    单词去重，找出所有不重复的单词，目的是为了构建特征向量
    :param dataset: 输入的数据集
    :return: 所有不重复的单词
    """
    vocab_set = set([])
    for document in dataset:
        vocab_set = vocab_set | set(document)
    return list(vocab_set)


def set_of_word_2_vec(vocab_set, inputset):
    """
    将inputset输入数据转化为特征向量对应的值 1代表单词出现 0代表单词未出现
    :param vocab_set: 特征向量的名称 其实就是单个的单词
    :param inputset: 输入数据
    :return: 返回inputset数据的真正的特征向量
    """
    return_vec = [0] * len(vocab_set)
    for word in inputset:
        if word in vocab_set:
            # 将单词对应的位置置位1
            return_vec[vocab_set.index(word)] = 1
    return return_vec


def train_nb0(train_mat, train_category):
    """
    训练数据
    :param train_mat: 训练矩阵
    :param train_category: 标签数组
    :return:
    """
    # 获取训练样本中的数量
    number_train_docs = len(train_mat)
    # 获取特征向量的维数  eg：(10, 32) 32就是特征向量的维数
    num_words = len(train_mat[0])
    p_abusive = sum(train_category) / float(number_train_docs)
    # 统计p0的数量 无侮辱性词条
    p0_num = np.zeros(num_words)
    # 统计p1的数量 含有侮辱性词条
    p1_num = np.zeros(num_words)
    # p0的分母
    p0_denom = 0.0
    # p1的分母
    p1_denom = 0.0

    for i in range(number_train_docs):
        if train_category[i] == 1:
            # p1_num 是统计train_category为1时所有出现过的单词集齐出现过的次数
            # eg ：p1_num = [0. 0. 0. 1. 2. 0. 3. 1. 1. 0. 1. 1. 0. 0. 0. 0. 1. 0. 0. 0. 1. 2. 1. 0.
            #  0. 1. 1. 0. 0. 0. 1. 1.]
            p1_num += train_mat[i]
            # p1_denom 统计train_category为1时 所有出现过的单词的数量 我感觉这个有点多余 循环完 直接求sum(p1_num)不就可以吗
            p1_denom += sum(train_mat[i])
        else:
            p0_num += train_mat[i]
            p0_denom += sum(train_mat[i])
    p1_vect = p1_num / p1_denom
    p0_vect = p0_num / p0_denom

    return p0_vect, p1_vect, p_abusive


def train_nb1(train_mat, train_category):
    """
    改进版 训练数据
    :param train_mat: 训练矩阵
    :param train_category: 标签数组
    :return: p1_vect 为分类为1时 所有单词出现的概率 p0_vect为分类为0时 所有单词出现的概率
    """
    # 获取训练样本中的数量
    number_train_docs = len(train_mat)
    # 获取特征向量的维数  eg：(10, 32) 32就是特征向量的维数
    num_words = len(train_mat[0])
    # 统计侮辱性(train_category为1的数据)评论所占比例
    p_abusive = sum(train_category) / float(number_train_docs)
    # 极大似然概率 把分子初始化为1 分母初始化为标签数组中种类的数量 eg：[0, 1, 0, 1, 0, 1] 只有两种取值 所以分母取2
    # 统计p0的数量 无侮辱性词条
    p0_num = np.ones(num_words)
    # 统计p1的数量 含有侮辱性词条
    p1_num = np.ones(num_words)
    # p0的分母
    p0_denom = 2.0
    # p1的分母
    p1_denom = 2.0

    for i in range(number_train_docs):
        if train_category[i] == 1:
            # p1_num 是统计train_category为1时所有出现过的单词集齐出现过的次数
            # eg ：p1_num = [0. 0. 0. 1. 2. 0. 3. 1. 1. 0. 1. 1. 0. 0. 0. 0. 1. 0. 0. 0. 1. 2. 1. 0.
            #  0. 1. 1. 0. 0. 0. 1. 1.]
            p1_num += train_mat[i]
            # p1_denom 统计train_category为1时 所有出现过的单词的数量 我感觉这个有点多余 循环完 直接求sum(p1_num)不就可以吗
            p1_denom += sum(train_mat[i])
        else:
            p0_num += train_mat[i]
            p0_denom += sum(train_mat[i])
    # 为了便面下溢出 这里去对数
    # p1_vect = p1_num / p1_denom
    # p0_vect = p0_num / p0_denom
    p1_vect = np.log(p1_num / p1_denom)
    p0_vect = np.log(p0_num / p0_denom)

    return p0_vect, p1_vect, p_abusive


def classify_nb(vec2_classify, p0_vec, p1_vec, p_class1):
    """
    分类
    :param vec2_classify:
    :param p0_vec: 分类为0时 所有单词出现的概率
    :param p1_vec: 分类为1时 所有单词出现的概率
    :param p_class1:
    :return: 返回所属分类
    """
    p1 = np.sum(vec2_classify * p1_vec) + np.log(p_class1)
    p0 = np.sum(vec2_classify * p0_vec) + np.log(1 - p_class1)
    if p1 > p0:
        return 1
    else:
        return 0


def testing_nb():
    """
    测试数据
    :return:
    """
    # 获取测试数据
    list_post, list_class = load_dataset()
    # 获取list大数组中所有的单词去重
    my_vecab_list = create_vocab_list(list_post)
    train_mat = []
    for post_in_doc in list_post:
        # 将每条评论转化为特征矩阵 并保存到train_mat中
        train_mat.append(set_of_word_2_vec(my_vecab_list, post_in_doc))
    p0v, p1v, pab = train_nb1(np.array(train_mat), np.array(list_class))
    # 待测的评论
    # test_entry = ['love', 'my', 'dalmation']
    test_entry = ['stupid', 'garbage']
    # 将待测的评论转化为特征向量 1代表存在 0代表不存在
    this_doc = set_of_word_2_vec(my_vecab_list, test_entry)
    class_label = classify_nb(this_doc, p0v, p1v, pab)
    return class_label


def bag_of_words_2_vec(vocab_list, inputset):
    """
    词袋模型
    :param vocab_list:
    :param inputset:
    :return:
    """
    return_vec = [0] * len(vocab_list)
    for word in inputset:
        return_vec[vocab_list.index(word)] += 1
    return return_vec


def text_parse(big_string):
    """
    文本解析 将文本中的单词全部提取出来
    :param big_string:
    :return:
    """
    import re
    list_of_tokens = re.split(r'[\W*]', big_string)
    return [word.lower() for word in list_of_tokens if len(word) > 2]

"""
def spam_test():

    doc_list = []
    class_list = []
    full_text = []

    for i in range(1, 26):
        # 读取email路径下spam中邮件内容
        email_content = open('./data/email/spam/%d.txt' % i, encoding='gbk').read()
        # 将邮件内容转化为单词数组
        word_list = text_parse(email_content)
        # word_list 二维数组 里面的每一个数组中代表一封邮件的内容
        doc_list.append(word_list)
        # 一维数组 将邮件中所有单词保存到full_text中
        full_text.extend(word_list)
        class_list.append(1)

        email_content = open('./data/email/ham/%d.txt' % i, encoding='gbk').read()
        word_list = text_parse(email_content)
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
    voca_list = create_vocab_list(doc_list)
    train_mat = []
    train_class = []

    for doc_index in trainset:
        train_mat.append(set_of_word_2_vec(voca_list, doc_list[doc_index]))
        train_class.append(class_list[doc_index])

    # 训练数据
    p0v, p1v, p_spam = train_nb1(train_mat, train_class)
    # 统计正确的个数
    count = 0
    # 开始在测试集中验证结果是否正确
    for doc_index in testset:
        word_vec = set_of_word_2_vec(voca_list, doc_list[doc_index])
        if classify_nb(np.array(word_vec), p0v, p1v, p_spam) == class_list[doc_index]:
            # 统计正确的个数
            count += 1
    # 计算正确率
    correct_rate = 1.0 * count / len(testset)
    return correct_rate

"""
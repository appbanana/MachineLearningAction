import bayes
import numpy as np
import feedparser
import operator
import collections


def cal_most_freq(vocab_list, full_text):
    """
    计算高频词汇
    :param vocab_list:
    :param full_text:
    :return:
    """
    freq_dict = collections.defaultdict(int)
    for token in vocab_list:
        freq_dict[token] = full_text.count(token)
    sorted_freq = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_freq[:30]


def local_words(feed1, feed0):
    """
    这个跟邮件spam_test非常相似 只是多了一个计算高频词汇模块(cal_most_freq) 一个词袋模型(bayes.bag_of_words_2_vec)
    :param feed1:
    :param feed0:
    :return:
    """
    doc_list = []
    class_list = []
    full_text = []
    mini_len = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(mini_len):
        word_list = bayes.text_parse(feed1['entries'][0]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)

        word_list = bayes.text_parse(feed0['entries'][0]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    # 所有不重复的单词构成特征向量
    voca_list = bayes.create_vocab_list(doc_list)
    # 计算高频词汇 并取出前30个 里面是元祖[(a, b), (c, d)...]
    top30_words = cal_most_freq(voca_list, full_text)
    for partW in top30_words:
        if partW[0] in voca_list:
            voca_list.remove(partW[0])

    training_set = range(2 * mini_len)
    testset = []
    # 下面for循环 随机挑选测试数据并加入的测试集中
    for i in range(20):
        rand_index = int(np.random.uniform(0, len(training_set)))
        testset.append(training_set[rand_index])
        del training_set[rand_index]
    train_mat = []
    train_class = []
    # 这个for循环训练数据
    for doc_index in training_set:
        train_mat.append(bayes.bag_of_words_2_vec(voca_list, doc_list[doc_index]))
        train_class.append(class_list[doc_index])
    #
    p0V, p1V, p_spam = bayes.train_nb1(np.array(train_mat), np.array(train_class))

    # 下面开始在测试集中验证 并计算准确率
    count = 0
    for doc_index in testset:
        word_vec = bayes.bag_of_words_2_vec(voca_list, doc_list[doc_index])
        class_label = bayes.classify_nb(word_vec, p0V, p1V, p_spam)
        if class_label == class_list[doc_index]:
            count += 1
    rate = 1.0 * count / len(testset)
    return rate


if __name__ == '__main__':
    # 因为entries 没有对应的数据 就没有进行测试验证
    ny = feedparser.parse('https://newyork.craigslist.org/mnh/index.rss')
    print(ny)

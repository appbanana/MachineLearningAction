import warnings
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn import ensemble

warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # 加载数据
    data = pd.read_csv('./data/Taitanic_data/data.csv')
    print(data.head())
    # (891, 12)
    print(data.isnull().sum())
    # 删除没用的
    data.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], inplace=True, axis=1)
    # 处理缺失值
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    # 删除有缺失值的
    data.dropna()
    # 将男性置位1 女性置位0
    data['Sex'] = (data['Sex'] == 'male').astype('int')
    labels = data['Embarked'].unique().tolist()
    print(data['Embarked'].unique().tolist())
    data['Embarked'] = data['Embarked'].apply(lambda x: labels.index(x))
    print(data.head())
    print(data.shape)
    # 提取特征矩阵和标签矩阵
    X = data.iloc[:, data.columns != "Survived"]
    y = data.iloc[:, data.columns == "Survived"]

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25)

    # 创建adaBoost模型
    # 元分类器默认的是深度为1的决策树
    ada = ensemble.AdaBoostClassifier(n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=66)
    ada = ada.fit(X_train, y_train)
    test_ada_score = ada.score(X_test, y_test)
    # 准确率：0.7982062780269058
    print('准确率：', test_ada_score)

    # 交叉验证
    scores = model_selection.cross_val_score(ada, X_train, y_train, cv=10)
    # 平均准确率： 0.7965240641711229
    print('平均准确率：', scores.mean())

    # 随机森林
    rfc = ensemble.RandomForestClassifier(n_estimators=100, random_state=66)
    rfc = rfc.fit(X_train, y_train)
    rfc_score = rfc.score(X_test, y_test)
    # 随机森林的准确率： 0.8026905829596412
    print('随机森林的准确率：', rfc_score)

    # 梯度提升
    gbc = ensemble.GradientBoostingClassifier(random_state=30).fit(X_train, y_train)
    score = gbc.score(X_test, y_test)
    # 梯度提升的准确率： 0.8475336322869955
    print('梯度提升的准确率：', score)

    # adaBoost与随机森林结合
    rfc = ensemble.RandomForestClassifier(n_estimators=100, random_state=88, n_jobs=-1)
    ada_rfc = ensemble.AdaBoostClassifier(rfc, n_estimators=100).fit(X_train, y_train)
    score = ada_rfc.score(X_test, y_test)
    # adaBoost与随机森林结合准确率： 0.7757847533632287
    print('adaBoost与随机森林结合准确率：', score)


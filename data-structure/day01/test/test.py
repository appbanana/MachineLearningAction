import spam
from spam import read1
# from glance.api import version as vs
from ..glance.api import version as vs


# 测试import模块
if __name__ == '__main__':
    # print(spam.read1())
    print(read1())
    print(vs.test_manage())

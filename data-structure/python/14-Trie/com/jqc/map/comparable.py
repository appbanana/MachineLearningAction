# 利用abc模块实现抽象类
import abc

"""
抽象类,用于两个对象的比较,实际上就是个比较器,相当于一个接口
"""


class Comparable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compare_to(self, o) -> int:
        pass

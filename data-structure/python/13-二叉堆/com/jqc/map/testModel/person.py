# https://blog.csdn.net/anlian523/article/details/80910808
import operator
from ..comparable import Comparable


class Person(Comparable):
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__.__name__ != other.__class__.__name__:
            return False
        return self.name == other.name and self.age == other.age and self.height == other.height
    
    def __hash__(self) -> int:
        """
        hash的实现 参考java的实现
        :return:
        """
        hash_code = hash(self.age)
        hash_code += hash_code * 31 + hash(self.height)
        hash_code += hash_code * 31 + hash(self.name if self.name else 0)
        return hash(self.age)
    
    def compare_to(self, p):
        """
        自己写的比较方法 没有直接用系统的__le__, __gt__,原因这是基类object的方法,我没法判断自定义的类有没有实现
        所以自定义实现一个比较函数,便于我判断自定义类有没有实现自定义的比较器
        比较函数 如果外界有传自定义的比较函数，就使用自定义比较函数，如果没有传就使用系统自带的operator
        :param p:
        :return:
        """
        # 如果相等返回0 大于返回1 小于返回-1
        return 0 if operator.eq(self.age, p.age) else (1 if operator.gt(self.age, p.age) else -1)

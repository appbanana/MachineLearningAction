import abc
import operator


class AbstractHeap(metaclass=abc.ABCMeta):
    def __init__(self, cmp):
        self._comparator = cmp
        self._size = 0
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def compare(self, e1, e2):
        """
        比较函数 如果外界有传自定义的比较函数，就使用自定义比较函数，如果没有传就使用系统自带的operator
        (ps:python3中没有cmp比较函数)
        :param e1:
        :param e2:
        :return:
        """
        if self._comparator is not None:
            #
            return self._comparator(e1, e2)
        # 如果相等返回0 大于返回1 小于返回-1
        return 0 if operator.eq(e1, e2) else (1 if operator.gt(e1, e2) else -1)

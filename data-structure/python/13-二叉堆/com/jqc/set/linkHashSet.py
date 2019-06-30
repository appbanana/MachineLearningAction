from .set import BaseSet
from com.jqc.map.linkHashMap import LinkHashMap

"""
思路 使用HashMap来实现
"""


class LinkHashSet(BaseSet):
    def __init__(self):
        self.__hash_map = LinkHashMap()
    
    def size(self) -> int:
        return self.__hash_map.size()
    
    def is_empty(self) -> bool:
        return self.__hash_map.is_empty()
    
    def is_contains(self, key) -> bool:
        return self.__hash_map.contains(key)
    
    def add(self, key):
        self.__hash_map.put(key, None)
    
    def remove(self, key):
        self.__hash_map.remove(key)
    
    def traversal(self, visit=None):
        """
        def visit(e):
            print(e)
            return True if e == 10 else False
        :param visit: lambda函数， 类似于上面形式的
        :return:
        """
        # assert visit is not None, "visit不能为空，请传入一个lambda函数"
        
        return self.__hash_map.traversal(visit)

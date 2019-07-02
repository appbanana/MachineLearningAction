from com.jqc.map.hashMap import HashMap
from collections import defaultdict


class Node(object):
    
    def __init__(self, parent):
        self.parent = parent
        self.character = None
        # children是HashMap类型,key值为字符类型,value为node类型
        self.children = None
        self.value = None
        # 用来标记是否是个单词
        self.word = False


class Trie(object):
    
    def __init__(self):
        self.__size = 0
        self.__root = None
    
    def size(self) -> int:
        return self.__size
    
    def clear(self):
        self.__root = None
        self.__size = 0
    
    def get(self, key):
        """
        根据key获取对应的value
        :param key:
        :return:
        """
        node = self.__node(key)
        return node.value if node else None
    
    def add(self, key, value):
        self.__key_check(key)
        if self.__root is None:
            self.__root = Node(None)
        
        node = self.__root
        for char in key:
            # 根据字符获取对应的node
            child_node = node.children.get(char) if node.children else None
            if child_node is None:
                child_node = Node(node)
                child_node.character = char
                # node.children原来存在更新新值,不存在创建HashMap
                node.children = node.children if node.children else HashMap()
                node.children.put(char, child_node)
            
            node = child_node
        
        if node.word:
            # 如果之前单词已经存在 覆盖并返回
            old_val = node.value
            node.value = value
            return old_val
        
        # 不存在 则添加
        node.word = True
        node.value = value
        self.__size += 1
        return None
    
    def remove(self, key):
        self.__key_check(key)
        node = self.__node(key)

        # 如果node不是以单词结尾 不做任何处理
        if node is None or not node.word:
            return
        self.__size -= 1
        old_value = node.value
        
        # 如果被删除的字符串是某个字符串的前缀, 只需要把word标记改为False,value清除
        if node.children and not node.children.is_empty():
            node.word = False
            node.value = None
            return old_value
        parent = node.parent
        while parent:
            parent.children.remove(node.character)
            # 一直删到他的父节点是某个单词的结尾或者这个父节点的children还有其他映射
            if parent.word or not parent.children.is_empty():
                break
                
            parent = parent.parent
        
        return old_value
    
    def start_with_string(self, prefix):
        """
        以某个字符开头
        :param prefix:
        :return:
        """
        return self.__node(prefix) is not None
    
    def contains(self, key):
        """
        是否包含某个单词
        :return:
        """
        node = self.__node(key)
        return node and node.word
    
    def __node(self, key):
        """
        更加key寻找对应的node
        :param key:
        :return:
        """
        self.__key_check(key)
        
        node = self.__root
        for char in key:
            if node is None or node.children is None or node.children.is_empty():
                return None
            node = node.children.get(char)
        return node
    
    @staticmethod
    def __key_check(key):
        if key is None or len(key) == 0:
            raise NameError('键不能为空')

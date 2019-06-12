# from typing import Callable
# from typing import TypeVar, Generic, NewType
# UserId = NewType('next', Node)
# T = TypeVar('T')

# from com.jqc.abstractList import AbstractList
"""
单链表
"""
from com.jqc.abstractList import AbstractList


class Node(object):
	def __init__(self, element=None, next_node=None):
		self.element = element
		self.next = next_node
	
	def __str__(self):
		return str(self.element)


class SingleLinkList(AbstractList):
	
	def __init__(self):
		super().__init__()
		self.__fist = None
	
	def __str__(self):
		"""
		自定义打印
		:return:
		"""
		string = 'size=' + str(self._size) + ", ["
		node = self.__fist
		for i in range(self._size):
			if i != 0:
				string += ','
			string += str(node.element)
			node = node.next
		string += ']'
		return string
	
	def index_of(self, element):
		"""
		获取链表中某个元素的索引
		:param element:
		:return:
		"""
		node = self.__fist
		for i in range(self._size):
			if node.element == element:
				return i
			node = node.next
		return -1
	
	def get(self, index):
		"""
		根据索引获取指定位置的元素
		:param index:
		:return:
		"""
		node = self.__node(index)
		return node.element
	
	def set(self, index, element):
		"""
		修改指定位置的元素
		:param index: 索引
		:param element: 新元素
		:return:
		"""
		node = self.__node(index)
		old_val = node.element
		node.element = element
		return old_val
	
	def insert(self, index, element):
		"""
		在指定位置插入元素
		:param index: 索引
		:param element: 元素
		"""
		self._range_check_add(index)
		if index == 0:
			self.__fist = Node(element, self.__fist)
		else:
			pre = self.__node(index - 1)
			pre.next = Node(element, pre.next)
		
		self._size += 1
	
	def remove(self, index):
		"""
		删除指定位置的节点
		:param index: 索引
		:return: 返回删除节点的元素
		"""
		self._range_check(index)
		node = self.__fist
		if index == 0:
			self.__fist = node.next
		else:
			pre = self.__node(index - 1)
			node = pre.next
			pre.next = node.next
		self._size -= 1
		return node.element
	
	def __node(self, index):
		"""
		根据索引获取node节点
		:param index:
		:return:
		"""
		self._range_check(index)
		node = self.__fist
		for i in range(index):
			node = node.next
		return node

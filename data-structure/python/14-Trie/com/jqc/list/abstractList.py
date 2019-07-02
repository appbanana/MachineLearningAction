# from abc import ABCMeta, abstractmethod


# class AbstractList(metaclass=ABCMeta):
class AbstractList(object):
	
	def __init__(self):
		self._size = 0
	
	def size(self) -> int:
		"""
		返回链表长度
		:return:
		"""
		return self._size
	
	def is_empty(self):
		"""
		链表是否为空
		:return:
		"""
		return self._size == 0
	
	def contains(self, element):
		"""
		链表是否包含某个元素
		:param element:
		:return:
		"""
		return self.index_of(element) != -1
	
	def add(self, element):
		"""
		链表增加节点
		:param element: 元素
		"""
		self.insert(self._size, element)
	
	def _range_check(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index >= self._size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self._size))
	
	def _range_check_add(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index > self._size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self._size))

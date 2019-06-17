from .abstractList import AbstractList


class DynamicArray(AbstractList):
	
	def __init__(self, capacity=10):
		super().__init__()
		self.__elements = [None] * (10 if capacity < 10 else capacity)
	
	def __str__(self):
		return f"size: {self._size}, capacity: {len(self.__elements)}\n{str(self.__elements[:self._size])}"
	
	def clear(self):
		"""
		清空
		:return:
		"""
		self.__elements = [None for _ in self.__elements]
		self._size = 0
	
	def add(self, element):
		"""
		添加元素
		:param element:
		:return:
		"""
		self.insert(self._size, element)
	
	def insert(self, index, element):
		"""
		插入元素
		:param index:
		:param element:
		:return:
		"""
		self._range_check_add(index)
		self.__ensure_capacity(self._size + 1)
		for i in range(self._size - 1, index - 1, -1):
			self.__elements[i + 1] = self.__elements[i]
		self.__elements[index] = element
		self._size += 1
	
	def get(self, index=0):
		"""
		根据索引获取元素
		:param index: 索引下标
		:return:
		"""
		self._range_check(index)
		
		return self.__elements[index]
	
	def set(self, index, element):
		"""
		更新指定位置的值
		:param index:
		:param element:
		:return: 返回原来的值
		"""
		self._range_check(index)
		old_val = self.__elements[index]
		self.__elements[index] = element
		return old_val
	
	def remove(self, index=0):
		"""
		删除指定索引位置的元素
		:param index: 索引
		:return: 返回删除的元素
		"""
		self._range_check(index)
		old_val = self.__elements[index]
		for i in range(index + 1, self._size):
			self.__elements[i - 1] = self.__elements[i]
		self.__elements[self._size - 1] = None
		self._size -= 1
		return old_val
	
	def index_of(self, element):
		"""
		判断element 是否存在
		:param element:
		:return:
		"""
		
		for index, item in enumerate(self.__elements):
			if element == item:
				return index
		return -1
	
	def __ensure_capacity(self, capacity):
		"""
		扩容
		:param capacity:
		:return:
		"""
		old_len = len(self.__elements)
		if old_len >= capacity:
			return
		new_capacity = old_len + (old_len >> 1)
		print('扩容', old_len, new_capacity)
		new_data = [None] * new_capacity
		new_data[:self._size] = self.__elements[:self._size]
		self.__elements = new_data

class DynamicArray(object):
	
	def __init__(self, capacity=5):
		self.__size = 0  # size
		self.__elements = [None] * (5 if capacity < 5 else capacity)
	
	def __str__(self):
		return f"size: {self.__size}, capacity: {len(self.__elements)}\n{str(self.__elements[:self.__size])}"
	
	def clear(self):
		"""
		清空
		:return:
		"""
		self.__elements = [None for _ in self.__elements]
		self.__size = 0
	
	def size(self):
		"""
		返回动态数组大小
		:return: 返回len(self.__elements)
		"""
		return self.__size
	
	def is_empty(self):
		"""
		判断数组是否为空
		:return: bool 值
		"""
		return self.__size == 0
	
	def contains(self, element):
		"""
		判断是否包含某个元素
		:param element: 元素
		:return:
		"""
		return self.index_of(element) != -1
	
	def add(self, element):
		"""
		添加元素
		:param element:
		:return:
		"""
		self.insert(self.__size, element)
	
	def insert(self, index, element):
		"""
		插入元素
		:param index:
		:param element:
		:return:
		"""
		self.__range_check_add(index)
		self.__ensure_capacity(self.__size + 1)
		for i in range(self.__size - 1, index - 1, -1):
			self.__elements[i + 1] = self.__elements[i]
		self.__elements[index] = element
		self.__size += 1
	
	def get(self, index=0):
		"""
		根据索引获取元素
		:param index: 索引下标
		:return:
		"""
		self.__range_check(index)
		
		return self.__elements[index]
	
	def set(self, index, element):
		"""
		更新指定位置的值
		:param index:
		:param element:
		:return: 返回原来的值
		"""
		self.__range_check(index)
		old_val = self.__elements[index]
		self.__elements[index] = element
		return old_val
	
	def remove(self, index=0):
		"""
		删除指定索引位置的元素
		:param index: 索引
		:return: 返回删除的元素
		"""
		self.__range_check(index)
		old_val = self.__elements[index]
		for i in range(index+1, self.__size):
			self.__elements[i-1] = self.__elements[i]
		self.__elements[self.__size - 1] = None
		self.__size -= 1
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
		new_data[:self.__size] = self.__elements[:self.__size]
		self.__elements = new_data
	
	def __range_check(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index >= self.__size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))
	
	def __range_check_add(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index > self.__size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))

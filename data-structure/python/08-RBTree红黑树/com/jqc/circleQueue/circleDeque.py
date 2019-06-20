"""
循环双端队列
"""


class CircleDeque(object):
	
	def __init__(self, capacity=10):
		# 存放数组首元素的下标
		self.__front = 0
		self.__size = 0
		self.__elements = [None] * (10 if capacity < 10 else capacity)
	
	def __str__(self):
		string = 'capcacity=' + str(len(self.__elements)) + ', size=' + str(self.__size)
		string += ', 起始索引 front = ' + str(self.__front)
		string += ', ['
		for i in range(0, len(self.__elements)):
			if i != 0:
				string += ','
			string += str(self.__elements[i])
		string += ']'
		
		return string
	
	def size(self) -> int:
		"""
		返回循环双端队列的长度
		:return:
		"""
		return self.__size
	
	def clear(self):
		"""
		清空循环双端队列
		:return:
		"""
		self.__elements = [None for _ in self.__elements]
		self.__front = 0
		self.__size = 0
	
	def is_empty(self) -> bool:
		"""
		判断循环双端队列是否为空
		:return: bool
		"""
		return self.__size == 0
	
	def en_queue_front(self, element):
		"""
		从队头入队列
		:param element: 元素
		:return:
		"""
		self.__ensure_capacity(self.__size + 1)
		# 这要注意一下
		# real_index = self.__index(0)
		self.__front = self.__index(-1)
		self.__elements[self.__front] = element
		self.__size += 1
	
	def en_queue_rear(self, element):
		"""
		从队尾入队列
		:param element: 元素
		:return:
		"""
		self.__ensure_capacity(self.__size + 1)
		real_index = self.__index(self.__size)
		self.__elements[real_index] = element
		self.__size += 1
	
	def de_queue_front(self):
		"""
		从队头出队列
		:return:
		"""
		old_element = self.__elements[self.__front]
		real_index = self.__index(0)
		self.__elements[real_index] = None
		self.__size -= 1
		self.__front = self.__index(1)
		
		return old_element
	
	def de_queue_rear(self):
		"""
		从队尾出队列
		:return:
		"""
		# real_index = self.__index(self.__size)
		real_index = self.__index(self.__size - 1)
		old_element = self.__elements[real_index]
		self.__elements[real_index] = None
		self.__size -= 1
		return old_element
	
	def front(self):
		"""
		查看队列头部元素
		:return:
		"""
		return self.__elements[self.__front]
	
	def rear(self):
		"""
		查看队列尾部元素
		:return:
		"""
		real_index = self.__index(self.__size)
		return self.__elements[real_index]
	
	def __ensure_capacity(self, capacity):
		"""
		扩容
		:param capacity: 新的容量大小
		:return:
		"""
		old_capacity = len(self.__elements)
		if old_capacity >= capacity:
			# 老的容量够用，不做任何处理
			return
		# 下面容量不够用，扩容
		new_capacity = old_capacity + (old_capacity >> 1)
		new_data = [None] * new_capacity
		# 这一定要注意 索引转化为真实的索引后在转移到新数组中
		new_data[:self.__size] = [self.__elements[self.__index(i)] for i in range(self.__size)]
		self.__elements = new_data
		# 扩容后要重置索引
		self.__front = 0
	
	def __index(self, index):
		"""
		将传入的索引转化为真正的索引
		:param index: 原来的索引
		:return: 真正的索引
		-1 % 5 = 4 所以对于负数不用管
		"""
		return (self.__front + index) % len(self.__elements)

"""
双链表
"""
from com.jqc.abstractList import AbstractList


class Node(object):
	def __init__(self, pre_node=None, element=None, next_node=None):
		self.pre = pre_node
		self.element = element
		self.next = next_node
	
	def __str__(self):
		"""
		自定义字符串输出函数 方便自己查看双链表的前后节点
		:return:
		"""
		string = ''
		string += 'None' if self.pre is None else str(self.pre.element)
		string += '_'
		string += str(self.element)
		string += '_'
		string += 'None' if self.next is None else str(self.next.element)
		return string


class LinkList(AbstractList):
	
	def __init__(self):
		super().__init__()
		self.__fist = None
		self.__last = None
	
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
			string += node.__str__()
			node = node.next
		string += ']'
		return string
	
	def clear(self):
		"""
		清空双链表元素
		"""
		self._size = 0
		self.__fist = None
		self.__last = None
	
	def insert(self, index, element):
		"""
		插入元素或在尾部添加节点
		:param index: 索引
		:param element: 元素
		"""
		self._range_check_add(index)
		if index == self._size:
			# 能进到这里，可能是第0个 也可能是添加到最后
			old_last = self.__last
			self.__last = Node(old_last, element, None)
			if old_last is None:
				# 第0个元素 首次添加元素
				self.__fist = self.__last
			else:
				# 在尾部添加节点
				old_last.next = self.__last
		else:
			next_node = self.__node(index)
			pre_node = next_node.pre
			current = Node(pre_node, element, next_node)
			next_node.pre = current
			
			if pre_node is None:
				# 如果pre为None 说明是第一个元素
				self.__fist = current
			else:
				pre_node.next = current
		
		self._size += 1
	
	def get(self, index):
		"""
		根据索引获取元素
		:param index:
		:return:
		"""
		node = self.__node(index)
		return node.element
	
	def set(self, index, element):
		"""
		更新节点元素
		:param index: 索引
		:param element: 元素
		:return: 返回原来的元素
		"""
		node = self.__node(index)
		old_val = node.element
		node.element = element
		return old_val
	
	def remove(self, index):
		"""
		删除指定节点的元素
		:param index:
		:return:
		"""
		current = self.__node(index)
		pre_node = current.pre
		next_node = current.next
		if pre_node is None:
			# 如果pre_node 为None 则删除的节点为首节点
			self.__fist = next_node
		else:
			pre_node.next = next_node
		
		if next_node is None:
			# 如果next_node 为None 则删除的节点为尾节点
			self.__last = pre_node
		else:
			next_node.pre = pre_node
		self._size -= 1
		return current.element
	
	def __node(self, index):
		"""
		当前index索引和self._size的一半比较 如果小于它的一半 从前往后开始遍历 否则从后往前倒着遍历
		:param index:
		:return:
		"""
		self._range_check(index)
		# self._size >> 1 self._size大小右移一位，就是除以2
		half = (self._size >> 1)
		if index < half:
			node = self.__fist
			for i in range(index):
				node = node.next
			return node
		else:
			node = self.__last
			for i in range(self._size - 1, index, -1):
				node = node.pre
			return node

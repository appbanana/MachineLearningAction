from .set import BaseSet
from com.jqc.list.doubleLinkList import LinkList
"""
思路 使用双链表来实现
"""


class ListSet(BaseSet):
	
	def __init__(self):
		self.__link = LinkList()
	
	def __str__(self):
		size = self.size()
		string = 'size=' + str(size) + ', ['
		for i in range(size):
			string += str(self.__link.get(i))
			if i != (size - 1):
				string += ','
		string += ']'
		return string
	
	def size(self) -> int:
		return self.__link.size()
	
	def is_empty(self) -> bool:
		return self.__link.is_empty()
	
	def is_contains(self, element) -> bool:
		return self.__link.contains(element)
	
	def add(self, element):
		index = self.__link.index_of(element)
		if index == LinkList.ELEMENT_NOT_FOUND:
			self.__link.add(element)
		else:
			self.__link.set(index, element)
	
	def remove(self, element):
		index = self.__link.index_of(element)
		if index != LinkList.ELEMENT_NOT_FOUND:
			self.__link.remove(index)
	
	def traversal(self, visit=None):
		"""
		def visit(e):
			print(e)
			return True if e == 10 else False
		:param visit: lambda函数， 类似于上面形式的
		:return:
		"""
		# assert visit is not None, "visit不能为空，请传入一个lambda函数"
		
		size = self.size()
		container = []
		for i in range(size):
			container.append(self.__link.get(i))
			if visit and visit(self.__link.get(i)):
				return container
		return container

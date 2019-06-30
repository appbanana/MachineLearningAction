from .set import BaseSet
from com.jqc.binaryTree.rbTree import RBTree

"""
思路 使用红黑树来实现
"""


class TreeSet(BaseSet):
	
	def __init__(self, cmp=None):
		self.__rbtree = RBTree(cmp)
	
	def size(self) -> int:
		return self.__rbtree.size()
	
	def is_empty(self) -> bool:
		return self.__rbtree.is_empty()
	
	def is_contains(self, element) -> bool:
		return self.__rbtree.contains(element)
	
	def add(self, element):
		self.__rbtree.add(element)
	
	def remove(self, element):
		self.__rbtree.remove(element)
	
	def traversal(self, visit=None):
		"""
		def visit(e):
			print(e)
			return True if e == 10 else False
		:param visit: lambda函数， 类似于上面形式的
		:return:
		"""
		# assert visit is not None, "visit不能为空，请传入一个lambda函数"
		
		return self.__rbtree.level_order_tranversal(visit)

"""
二叉搜索树
"""

from typing import TypeVar
import operator
from .binaryTree import BinaryTree, Node

T = TypeVar('T')


class BinarySearchTree(BinaryTree):
	
	def __init__(self, comparator=None):
		super().__init__()
		# self._size = 0
		# self._root = None
		self._comparator = comparator
	
	def __str__(self):
		"""
		自定义输出函数 中序遍历输出
		:return:
		"""
		self.inorder()
		container = []
		self.__to_string(self._root, container, '')
		string = ''
		for item in container:
			string += item
		return string
	
	def __to_string(self, node: Node, container: list, prefix: str):
		"""
		中序遍历输出
		"""
		if node is None:
			return
		self.__to_string(node.left, container, prefix + 'L---')
		container.append(prefix)
		container.append(str(node.element))
		container.append('\n')
		self.__to_string(node.right, container, prefix + 'R---')
	
	def contains(self, element) -> bool:
		"""
		是否包含某个元素
		:param element:
		:return:
		"""
		return self.__node(element) is not None
	
	def add(self, element) -> None:
		"""
		添加元素
		:param element:
		:return:
		"""
		self.__element_not_none_check(element)
		# 添加第一个节点 第一个节点即为根节点
		if self._root is None:
			# self._root = Node(element, None)
			self._root = self.create_node(element, None)
			self._size += 1
			self.after_add(self._root)
			return
		
		# 不是第一个节点
		node = self._root
		while node is not None:
			# 暂时保存上一个节点 上一个节点即为下一个的父节点 下面会用到
			parent = node
			# 记录比较的大小
			# cmp = element - node.element
			cmp = self.__compare(element, node.element)
			if cmp > 0:
				# 大于 往右子树找
				node = node.right
			elif cmp < 0:
				# 小于0 往左子树找
				node = node.left
			else:
				return
		# new_node = Node(element, parent)
		new_node = self.create_node(element, parent)
		
		if cmp > 0:
			parent.right = new_node
		else:
			parent.left = new_node
		self._size += 1
		self.after_add(new_node)
	
	def remove(self, element) -> T:
		"""
		删除元素对应的节点
		:param element:
		:return:
		"""
		return self.__remove(self.__node(element))
	
	def create_node(self, element, parent) -> Node:
		"""
		创建一个节点，默认创建一个node节点，可有子类去实现，返回对应的node
		:return:
		"""
		return Node(element, parent)
	
	def after_add(self, node: Node) -> None:
		"""
		添加节点之后的操作，交给子类去实现，用于修复avl树的平衡或者去修复红黑树的性质
		:return:
		"""
		pass
	
	def after_remove(self, node: Node) -> None:
		"""
		删除节点之后的操作，交给子类去实现，用于修复avl树的平衡或者去修复红黑树的性质
		:return:
		"""
		pass
	
	def __remove(self, node: Node):
		"""
		删除节点
		:param node:
		:return:
		"""
		if node is None:
			return
		
		old_val = node.element
		
		# 度为2的节点直接删除它的前驱或者后继
		# 在这里我们删除的是后继节点
		if node.has_two_children():
			# 找到后继节点
			s = self.successor(node)
			# 将后继节点的值赋值给node的element
			node.element = s.element
			# 接下来让node指向s(后继节点)
			node = s
		
		# 下面删除就是度为0或者度为1的节点, 删除度为1的节点 直接让其子节点取代, 删除度为0的指点，直接删除即可
		replace_node = node.left if node.left else node.right
		if replace_node is not None:
			# 删除度为1的节点
			replace_node.parent = node.parent
			if node.parent is None:
				# 删除的是度为1的根节点
				self._root = replace_node
			elif node == node.parent.left:
				node.parent.left = replace_node
			else:
				node.parent.right = replace_node
			# 删除之后验证avl树
			self.after_remove(replace_node)
		elif node.parent is None:
			# 删除的是度为0的根节点
			self._root = None
			# 删除之后验证avl树
			self.after_remove(node)
		else:
			# 删除度为0的节点
			if node == node.parent.left:
				node.parent.left = None
			else:
				node.parent.right = None
			# 删除之后验证avl树
			self.after_remove(node)
		return old_val
	
	@staticmethod
	def __element_not_none_check(element):
		"""
		校验传入的元素
		:param element:
		:return:
		"""
		if element is None:
			raise NameError('element 不能为None')
	
	def __compare(self, e1, e2):
		"""
		比较函数 如果外界有传自定义的比较函数，就使用自定义比较函数，如果没有传就使用系统自带的operator
		(ps:python3中没有cmp比较函数)
		:param e1:
		:param e2:
		:return:
		"""
		if self._comparator is not None:
			#
			return self._comparator(e1, e2)
		# 如果相等返回0 大于返回1 小于返回-1
		return 0 if operator.eq(e1, 32) else (1 if operator.gt(e1, e2) else -1)
	
	def __node(self, element):
		"""
		根据传的的元素 获取对应node 节点
		:param element:
		:return:
		"""
		self.__element_not_none_check(element)
		node = self._root
		while node is not None:
			cmp = self.__compare(element, node.element)
			if cmp == 0:
				return node
			if cmp > 0:
				node = node.right
			else:
				node = node.left
		return node

from .binaryTree import Node
from .bbst import BBST


class AVLNode(Node):
	def __init__(self, element, parent) -> None:
		"""
		自定义初始化
		:param element: 元素
		:param parent: 父节点
		"""
		super().__init__(element, parent)
		# 记录节点的高度
		self.__height = 1
	
	def __str__(self):
		parent_string = 'none'
		if self.parent is not None:
			parent_string = str(self.parent.element)
		return str(self.element) + '_p(' + parent_string + ')_h(' + str(self.__height) + ')'
	
	def balance_factor(self) -> int:
		"""
		返回当前节点的平衡因子
		:return:
		"""
		
		left_height = 0 if self.left is None else self.left.__height
		right_height = 0 if self.right is None else self.right.__height
		return left_height - right_height
	
	def update_height(self) -> None:
		"""
		更新节点高度
		:return:
		"""
		left_height = 0 if self.left is None else self.left.__height
		right_height = 0 if self.right is None else self.right.__height
		self.__height = 1 + max(left_height, right_height)
	
	def taller_child(self) -> Node:
		"""
		返回左右子树中 最高的那个节点
		:return:
		"""
		left_height = 0 if self.left is None else self.left.__height
		right_height = 0 if self.right is None else self.right.__height
		if left_height > right_height:
			return self.left
		if left_height < right_height:
			return self.right
		return self.left if self.is_left_child() else self.right


class AVLTree(BBST):
	
	def create_node(self, element, parent) -> Node:
		"""
		重写父类的方法，返回一个AVLNode 节点
		:param element:
		:param parent:
		:return:
		"""
		return AVLNode(element, parent)
	
	def after_add(self, node: Node) -> None:
		"""
		添加节点之后，修复avl平衡树的性质
		:return:
		"""
		node = node.parent
		while node is not None:
			if self.__is_balanced(node):
				# 如果avl树是平衡的 更新高度
				node.update_height()
			else:
				# 否则 再度恢复平衡
				self.__rebalance(node)
				break
			
			node = node.parent
	
	def after_remove(self, node: Node) -> None:
		"""
		删除节点之后的操作
		:param node:
		:return:
		"""
		node = node.parent
		while node is not None:
			if self.__is_balanced(node):
				node.update_height()
			else:
				self.__rebalance(node)
			
			node = node.parent
	
	def _after_rotate(self, grand: Node, parent: Node, child: Node):
		super()._after_rotate(grand, parent, child)
		grand.update_height()
		parent.update_height()
	
	@staticmethod
	def __is_balanced(node: Node) -> bool:
		"""
		判断左右子树高度的绝对值是否 <= 1
		:return:
		"""
		return abs(node.balance_factor()) <= 1
	
	def __rebalance(self, grand: Node):
		"""
		恢复平衡
		:param grand:
		:return:
		"""
		parent = grand.taller_child()
		node = parent.taller_child()
		
		if parent.is_left_child():
			# L
			if node.is_left_child():
				# LL 右旋
				self._rotate_right(grand)
			else:
				# LR 先对parent左旋在对grand右旋
				self._rotate_left(parent)
				self._rotate_right(grand)
		else:
			# R
			if node.is_left_child():
				# RL 先对parent右旋 在对grand左旋
				self._rotate_right(parent)
				self._rotate_left(grand)
			else:
				# RR 对grand左旋
				self._rotate_left(grand)


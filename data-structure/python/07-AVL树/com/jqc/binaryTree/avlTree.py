from .binarySearchTree import BinarySearchTree
from .binaryTree import Node


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


class AVLTree(BinarySearchTree):
	
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
				self.__rotate_right(grand)
			else:
				# LR 先对parent左旋在对grand右旋
				self.__rotate_left(parent)
				self.__rotate_right(grand)
		else:
			# R
			if node.is_left_child():
				# RL 先对parent右旋 在对grand左旋
				self.__rotate_right(parent)
				self.__rotate_left(grand)
			else:
				# RR 对grand左旋
				self.__rotate_left(grand)
	
	# def __rotate_left(self, grand: AVLNode):
	# 	"""
	# 	左旋转
	# 	:param node: 要旋转的节点
	# 	:return:
	# 	"""
	# 	parent = grand.right
	# 	child = parent.left
	#
	# 	grand.right = child
	# 	parent.left = grand
	#
	# 	# 更新grand，parent，child的父节点
	# 	# 更新parent的父节点
	# 	parent.parent = grand.parent
	# 	if grand.is_left_child():
	# 		# grand原来是它父节点的左子节点，就让grand.parent.left指向parent
	# 		grand.parent.left = parent
	# 	elif grand.is_right_child():
	# 		# grand原来是它父节点的右子节点，就让grand.parent.right指向parent
	# 		grand.parent.right = parent
	# 	else:
	# 		# grand既不是左子节点 又不是右子节点 如果grand的父节点是根节点
	# 		self._root = parent
	#
	# 	# 更新child, grand的父节点
	# 	if child is not None:
	# 		child.parent = grand
	# 	grand.parent = parent
	#
	# 	# 更新高度
	# 	grand.update_height()
	# 	parent.update_height()
	
	def __rotate_left(self, grand: Node):
		"""
		左旋转
		:param node: 要旋转的节点
		:return:
		"""
		parent = grand.right
		child = parent.left
		
		grand.right = child
		parent.left = grand
		
		self.__after_rotate(grand, parent, child)
	
	def __rotate_right(self, grand: Node):
		"""
		右旋选
		:param node: 要旋转的节点
		:return:
		"""
		parent = grand.left
		child = parent.right
		
		grand.left = child
		parent.right = grand
		
		# 封装后 直接使用这个方法代替下面一坨代码
		self.__after_rotate(grand, parent, child)
	
	def __after_rotate(self, grand: Node, parent: Node, child: Node):
		# 更新grand，parent，child的父节点
		# 更新parent的父节点
		parent.parent = grand.parent

		if grand.is_left_child():
			# grand原来是它父节点的左子节点，就让grand.parent.left指向parent
			grand.parent.left = parent
		elif grand.is_right_child():
			# grand原来是它父节点的右子节点，就让grand.parent.right指向parent
			grand.parent.right = parent
		else:
			# grand既不是左子节点 又不是右子节点 如果grand的父节点是根节点
			self._root = parent
		
		# 更新child, grand的父节点
		if child is not None:
			child.parent = grand
		grand.parent = parent
		
		# 更新高度
		grand.update_height()
		parent.update_height()

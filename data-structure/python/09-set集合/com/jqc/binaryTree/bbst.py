"""
BalanceBinarySearchTree
平衡二叉搜索树
"""

from .binarySearchTree import BinarySearchTree
from .binaryTree import Node


class BBST(BinarySearchTree):
	def _rotate_left(self, grand: Node):
		"""
		左旋转
		:param node: 要旋转的节点
		:return:
		"""
		parent = grand.right
		child = parent.left
		
		grand.right = child
		parent.left = grand
		
		self._after_rotate(grand, parent, child)
	
	def _rotate_right(self, grand: Node):
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
		self._after_rotate(grand, parent, child)
	
	def _after_rotate(self, grand: Node, parent: Node, child: Node):
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
